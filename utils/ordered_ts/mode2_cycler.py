# -*- coding: UTF-8 -*-
from utils.ordered_ts.mode4_cycler import work_cycle_4


def work_cycle_2(url, index_array, file_path, max_threads):
    work_cycle_4(url, index_array, '', file_path, max_threads, 2)
