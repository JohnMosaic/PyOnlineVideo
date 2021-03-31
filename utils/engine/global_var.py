# -*- coding: UTF-8 -*-

is_cycle_done = False


def set_value(value):
    global is_cycle_done
    is_cycle_done = value


def get_value():
    return is_cycle_done
