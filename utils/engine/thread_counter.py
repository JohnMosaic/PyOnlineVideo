# -*- coding: UTF-8 -*-
import threading

this_lock = threading.Lock()


class ThreadCounter:
    thread_number = 0

    def __init__(self, t_number):
        self.thread_number = t_number

    def read(self):
        this_lock.acquire()
        t_num = self.thread_number
        this_lock.release()
        return t_num

    def add(self):
        this_lock.acquire()
        self.thread_number += 1
        this_lock.release()

    def minus(self):
        this_lock.acquire()
        self.thread_number -= 1
        t_num = self.thread_number
        this_lock.release()
        if t_num <= 0:
            return 0
        return t_num
