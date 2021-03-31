# -*- coding: UTF-8 -*-
from utils.common.converter import index_converter
from utils.common.file_operator import record_log
from utils.engine.m3u8_parser import get_url_array_from_m3u8_file
from utils.engine.core_worker import thread_counter, do_work_a, do_work_b
import utils.engine.global_var as gv
import threading


def work_cycle_7(url_left_part, m3u8_file, key, file_path, max_threads, mode):
    url_dict = get_url_array_from_m3u8_file(url_left_part, m3u8_file, mode)
    url_count = len(url_dict)
    if url_count > 0:
        print('[INFO] Mode ' + str(mode) + ' work start.')
        record_log(
            'INFO',
            'Mode ' + str(mode) + ' work start.',
            'Work cycle'
        )
        length = len(str(url_count))
        thread_list = []
        for index in url_dict.keys():
            try:
                index_str = index_converter(index, length)
                if index_str != 'ERROR':
                    url = url_dict[index]
                    filename = index_str + '.ts'
                    while True:
                        count = thread_counter.read()
                        if count < max_threads:
                            thread_counter.add()
                            if mode == 5:
                                t5 = threading.Thread(
                                    target=do_work_a,
                                    args=(index_str, filename, url, file_path, 5)
                                )
                                t5.setDaemon(True)
                                thread_list.append(t5)
                                t5.start()
                            elif mode == 7:
                                vector = url[url.rfind('/')+1:]
                                t7 = threading.Thread(
                                    target=do_work_b,
                                    args=(index_str, filename, url, key, vector, file_path, 7)
                                )
                                t7.setDaemon(True)
                                thread_list.append(t7)
                                t7.start()
                            break
                        else:
                            for t in thread_list:
                                t.join()
                            thread_list.clear()
                else:
                    print('[ERROR] Mode ' + str(mode) + ' index ' + str(index) + ' convert failed...')
                    record_log(
                        'ERROR',
                        'Mode ' + str(mode) + ' index ' + str(index) + ' convert failed...',
                        'Work cycle' + str(index)
                    )
            except Exception as ex:
                print('[ERROR] Mode ' + str(mode) + ' cycle error: ' + str(ex) +
                      ' index ' + str(index) + ' work failed...')
                record_log(
                    'ERROR',
                    'Mode ' + str(mode) + ' cycle error: ' + str(ex),
                    'Work cycle ' + str(index)
                )
        gv.set_value(True)
    else:
        print('[WARN] Mode ' + str(mode) + " found none *.ts file's url in the m3u8 file...")
