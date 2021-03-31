# -*- coding: UTF-8 -*-
from utils.common.file_operator import record_log
from utils.engine.m3u8_parser import get_url_array_from_log_file
from utils.engine.core_worker import thread_counter, do_work_a, do_work_b
import utils.engine.global_var as gv
import threading


def work_cycle_8(log_file, key, file_path, max_threads, mode):
    url_dict = get_url_array_from_log_file(log_file, mode)
    url_count = len(url_dict)
    if url_count > 0:
        print('[INFO] Mode ' + str(mode) + ' work start.')
        record_log(
            'INFO',
            'Mode ' + str(mode) + ' work start.',
            'Work cycle'
        )
        thread_list = []
        for index_str in url_dict.keys():
            try:
                url = url_dict[index_str]
                filename = index_str + '.ts'
                while True:
                    count = thread_counter.read()
                    if count < max_threads:
                        thread_counter.add()
                        if mode == 6:
                            t6 = threading.Thread(
                                target=do_work_a,
                                args=(index_str, filename, url, file_path, 6)
                            )
                            t6.setDaemon(True)
                            thread_list.append(t6)
                            t6.start()
                        elif mode == 8:
                            vector = url[url.rfind('/')+1:]
                            t8 = threading.Thread(
                                target=do_work_b,
                                args=(index_str, filename, url, key, vector, file_path, 8)
                            )
                            t8.setDaemon(True)
                            thread_list.append(t8)
                            t8.start()
                        break
                    else:
                        for t in thread_list:
                            t.join()
                        thread_list.clear()
            except Exception as ex:
                print('[ERROR] Mode ' + str(mode) + ' cycle error: ' + str(ex) +
                      ' index ' + index_str + ' work failed...')
                record_log(
                    'ERROR',
                    'Mode ' + str(mode) + ' cycle error: ' + str(ex),
                    'Work cycle ' + index_str
                )
        gv.set_value(True)
    else:
        print('[WARN] Mode ' + str(mode) + " found none *.ts file's url in the log file...")
