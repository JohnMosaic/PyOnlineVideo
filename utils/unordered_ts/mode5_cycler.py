# -*- coding: UTF-8 -*-
from utils.unordered_ts.mode7_cycler import work_cycle_7


def work_cycle_5(url_left_part, m3u8_file, file_path, max_threads):
    work_cycle_7(url_left_part, m3u8_file, '', file_path, max_threads, 5)
