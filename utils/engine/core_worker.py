# -*- coding: UTF-8 -*-
from utils.common.aes_helper import aes_128_decrypt
from utils.common.file_operator import record_log, merge_files
from utils.common.networker import download_file_2_byte_array, write_byte_array_2_file
import utils.engine.global_var as gv
import utils.engine.thread_counter as tc


thread_counter = tc.ThreadCounter(0)
is_error_occurred = False


def do_work_a(index_str, filename, url, file_path, mode):
    try:
        network_byte_array = download_file_2_byte_array(url)
        if network_byte_array:
            write_file(index_str, filename, url, file_path, network_byte_array, mode)
        else:
            download_failed(index_str, url, mode)
    finally:
        work_done(url, file_path, mode)


def do_work_b(index_str, filename, url, key, vector, file_path, mode):
    try:
        network_byte_array = download_file_2_byte_array(url)
        if network_byte_array:
            decrypted_byte_array = aes_128_decrypt(network_byte_array, key, vector)
            if decrypted_byte_array:
                write_file(index_str, filename, url, file_path, decrypted_byte_array, mode)
            else:
                decrypted_failed(index_str, url, mode)
        else:
            download_failed(index_str, url, mode)
    finally:
        work_done(url, file_path, mode)


def write_file(index_str, filename, url, file_path, byte_array, mode):
    if mode == 1 or mode == 2 or mode == 3 or mode == 4:
        filename = url[url.rfind('/')+1:]
    full_path_name = file_path + '\\' + filename
    if not write_byte_array_2_file(byte_array, full_path_name):
        write_failed(index_str, url, mode)


def write_failed(index_str, url, mode):
    global is_error_occurred
    is_error_occurred = True
    print('[ERROR] Mode ' + str(mode) + ' write byte array failed... #' + index_str + '>' + url)
    record_log(
        'ERROR',
        'Mode ' + str(mode) + ' write byte array failed...',
        '#' + index_str + '>' + url
    )


def decrypted_failed(index_str, url, mode):
    global is_error_occurred
    is_error_occurred = True
    print('[ERROR] Mode ' + str(mode) + ' AES decrypt byte array failed... #' + index_str + '>' + url)
    record_log(
        'ERROR',
        'Mode ' + str(mode) + ' AES decrypt byte array failed...',
        '#' + index_str + '>' + url
    )


def download_failed(index_str, url, mode):
    global is_error_occurred
    is_error_occurred = True
    print('[ERROR] Mode ' + str(mode) + ' download file to byte array failed... #' + index_str + '>' + url)
    record_log(
        'ERROR',
        'Mode ' + str(mode) + ' download file to byte array failed...',
        '#' + index_str + '>' + url
    )


def work_done(url, file_path, mode):
    count = thread_counter.minus()
    if count == 0 and gv.get_value():
        if (mode == 1 or mode == 3 or mode == 5 or mode == 7) and not is_error_occurred:
            print('[INFO] Mode ' + str(mode) + ' download files done!')
            record_log(
                'INFO',
                'Mode ' + str(mode) + ' download files done!',
                'Download files'
            )
            tmp = url[url.rfind('/')+1:]
            filename = tmp[0:-3]
            merge_files(file_path, filename, mode)
        else:
            print('[INFO] Mode ' + str(mode) + ' download files done partly!')
            record_log(
                'INFO',
                'Mode ' + str(mode) + ' download files done partly!',
                'Download files'
            )
