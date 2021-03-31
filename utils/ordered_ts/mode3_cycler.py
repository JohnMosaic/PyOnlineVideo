# -*- coding: UTF-8 -*-
from utils.common.converter import index_converter
from utils.common.file_operator import record_log
from utils.engine.core_worker import thread_counter, do_work_a, do_work_b
import utils.engine.global_var as gv
import threading


def work_cycle_3(url, max_limit, key, file_path, max_threads, mode):
    print('[INFO] Mode ' + str(mode) + ' work start.')
    record_log(
        'INFO',
        'Mode ' + str(mode) + ' work start.',
        'Work cycle'
    )
    length = len(str(max_limit))
    thread_list = []
    for index in range(length + 1):
        try:
            index_str = index_converter(index, length)
            if index_str != 'ERROR':
                new_url = url[0:len(url)-length-3] + index_str + '.ts'
                while True:
                    count = thread_counter.read()
                    if count < max_threads:
                        thread_counter.add()
                        if mode == 1:
                            t1 = threading.Thread(
                                target=do_work_a,
                                args=(index_str, '', new_url, file_path, 1)
                            )
                            t1.setDaemon(True)
                            thread_list.append(t1)
                            t1.start()
                        elif mode == 3:
                            vector = new_url[new_url.rfind('/')+1:]
                            t3 = threading.Thread(
                                target=do_work_b,
                                args=(index_str, '', new_url, key, vector, file_path, 3)
                            )
                            t3.setDaemon(True)
                            thread_list.append(t3)
                            t3.start()
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
