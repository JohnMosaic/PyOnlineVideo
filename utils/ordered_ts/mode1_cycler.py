# -*- coding: UTF-8 -*-
from utils.ordered_ts.mode3_cycler import work_cycle_3


def work_cycle_1(url, max_limit, file_path, max_threads):
    work_cycle_3(url, max_limit, '', file_path, max_threads, 1)
