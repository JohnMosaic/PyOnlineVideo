# -*- coding: UTF-8 -*-
import os
import time


def check_max_limit(max_limit_str):
    try:
        return int(max_limit_str)
    except ValueError:
        print('[ERROR] The max_limit arg must be an integer type...')
        return 0


def check_max_threads(max_threads_str):
    try:
        return int(max_threads_str)
    except ValueError:
        print('[ERROR] The download max_threads arg must be an integer type...')
        return 0


def check_index_array(index_array_str):
    index_array = [-1]
    try:
        index_array_str = index_array_str.replace('[', '').replace(']', '')
        index_str_array = index_array_str.split(',')
        length = len(index_str_array)
        for i in range(length):
            index_array[i] = int(index_str_array[i])
    except ValueError:
        print('[ERROR] The index array arg must be an integer array type...')
    return index_array


def check_file_path(mode):
    file_path = os.getcwd() + '\\ts_files_mode_' + str(mode) + '_' + time.strftime('%Y%m%d%H%M%S', time.localtime())
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    return file_path


def check_file(filename, file_type):
    if not os.path.isfile(filename):
        print('[ERROR] The ' + file_type + ' file \"' + filename + '\" does not exists...')
        return False
    return True
