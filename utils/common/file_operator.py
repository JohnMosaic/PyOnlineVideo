# -*- coding: UTF-8 -*-
import os
import time

log_dir = os.getcwd() + '\\log\\'


def record_log(msg_type, msg, mark):
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    log_filename = log_dir + time.strftime('%Y_%m', time.localtime()) + '_online_video.log'
    f = open(log_filename, mode='a+', encoding='utf8')
    dt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    a = f'{dt}\r\n[{msg_type}]{msg} --> {mark}\r\n\r\n'
    f.write(a)
    f.close()


def merge_files(file_path, filename, mode):
    cmd = 'copy /b ' + file_path + '\\*.ts ' + file_path + '\\' + filename + '.mp4&exit'
    print('[INFO] Mode ' + str(mode) + ' merging files...')
    ret = os.popen(cmd)
    output_str = ret.read()
    print(output_str)
    record_log('INFO', 'Mode ' + str(mode) + ' merge log:\r\n' + output_str, 'Merge files')
