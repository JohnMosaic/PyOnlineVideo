# -*- coding: UTF-8 -*-
import sys
sys.path.append('..\\')
from control.usage import show_usage
from utils.ordered_ts.mode1_cycler import work_cycle_1
from utils.ordered_ts.mode2_cycler import work_cycle_2
from utils.ordered_ts.mode3_cycler import work_cycle_3
from utils.ordered_ts.mode4_cycler import work_cycle_4
from utils.unordered_ts.mode5_cycler import work_cycle_5
from utils.unordered_ts.mode6_cycler import work_cycle_6
from utils.unordered_ts.mode7_cycler import work_cycle_7
from utils.unordered_ts.mode8_cycler import work_cycle_8
import control.args_checker as ac


def main(argv):
    args_len = len(argv)
    if args_len == 4:
        mode = argv[1]
        if mode == '-su':
            log_file = argv[2]
            if ac.check_file(log_file, 'log'):
                max_threads = ac.check_max_threads(argv[3])
                if max_threads != 0:
                    file_path = ac.check_file_path(6)
                    work_cycle_6(log_file, file_path, max_threads)
                else:
                    show_usage()
            else:
                show_usage()
        else:
            show_usage()
    elif args_len == 5:
        mode = argv[1]
        if mode == '-d':
            url = argv[2]
            max_limit = ac.check_max_limit(argv[3])
            if max_limit != 0:
                max_threads = ac.check_max_threads(argv[4])
                if max_threads != 0:
                    file_path = ac.check_file_path(1)
                    work_cycle_1(url, max_limit, file_path, max_threads)
                else:
                    show_usage()
            else:
                show_usage()
        elif mode == '-sd':
            url = argv[2]
            index_array = ac.check_index_array(argv[3])
            if index_array[0] != -1:
                max_threads = ac.check_max_threads(argv[4])
                if max_threads != 0:
                    file_path = ac.check_file_path(2)
                    work_cycle_2(url, index_array, file_path, max_threads)
                else:
                    show_usage()
            else:
                show_usage()
        elif mode == '-u':
            url = argv[2]
            m3u8_file = argv[3]
            if ac.check_file(m3u8_file, 'm3u8'):
                max_threads = ac.check_max_threads(argv[4])
                if max_threads != 0:
                    file_path = ac.check_file_path(5)
                    work_cycle_5(url, m3u8_file, file_path, max_threads)
                else:
                    show_usage()
            else:
                show_usage()
        elif mode == '-sau':
            log_file = argv[2]
            if ac.check_file(log_file, 'log'):
                key = argv[3]
                max_threads = ac.check_max_threads(argv[4])
                if max_threads != 0:
                    file_path = ac.check_file_path(8)
                    work_cycle_8(log_file, key, file_path, max_threads, 8)
                else:
                    show_usage()
            else:
                show_usage()
        else:
            show_usage()
    elif args_len == 6:
        mode = argv[1]
        url = argv[2]
        if mode == '-ad':
            max_limit = ac.check_max_limit(argv[3])
            if max_limit != 0:
                key = argv[4]
                max_threads = ac.check_max_threads(argv[5])
                if max_threads != 0:
                    file_path = ac.check_file_path(3)
                    work_cycle_3(url, max_limit, key, file_path, max_threads, 3)
                else:
                    show_usage()
            else:
                show_usage()
        elif mode == '-sad':
            index_array = ac.check_index_array(argv[3])
            if index_array[0] != -1:
                key = argv[4]
                max_threads = ac.check_max_threads(argv[5])
                if max_threads != 0:
                    file_path = ac.check_file_path(4)
                    work_cycle_4(url, index_array, key, file_path, max_threads, 4)
                else:
                    show_usage()
            else:
                show_usage()
        elif mode == '-au':
            m3u8_file = argv[3]
            if ac.check_file(m3u8_file, 'm3u8'):
                key = argv[4]
                max_threads = ac.check_max_threads(argv[5])
                if max_threads != 0:
                    file_path = ac.check_file_path(7)
                    work_cycle_7(url, m3u8_file, key, file_path, max_threads, 7)
                else:
                    show_usage()
            else:
                show_usage()
        else:
            show_usage()
    else:
        show_usage()


if __name__ == '__main__':
    # sys.argv.append('-au')
    # sys.argv.append('https://video.*****.com/500kb/hls/')
    # sys.argv.append('D:\\Downloads\\index.m3u8')
    # sys.argv.append('f9de22d7bc9ea9da')
    # sys.argv.append('10')
    main(sys.argv)
