# -*- coding: UTF-8 -*-


def index_converter(index, length):
    if length == 1:
        if 0 <= index < 10:
            return str(index)
        else:
            return 'ERROR'
    elif length == 2:
        if 0 <= index < 10:
            return '0' + str(index)
        elif 10 <= index < 100:
            return str(index)
        else:
            return 'ERROR'
    elif length == 3:
        if 0 <= index < 10:
            return '00' + str(index)
        elif 10 <= index < 100:
            return '0' + str(index)
        elif 100 <= index < 1000:
            return str(index)
        else:
            return 'ERROR'
    elif length == 4:
        if 0 <= index < 10:
            return '000' + str(index)
        elif 10 <= index < 100:
            return '00' + str(index)
        elif 100 <= index < 1000:
            return '0' + str(index)
        elif 1000 <= index < 10000:
            return str(index)
        else:
            return 'ERROR'
    elif length == 5:
        if 0 <= index < 10:
            return '0000' + str(index)
        elif 10 <= index < 100:
            return '000' + str(index)
        elif 100 <= index < 1000:
            return '00' + str(index)
        elif 1000 <= index < 10000:
            return '0' + str(index)
        elif 10000 <= index < 100000:
            return str(index)
        else:
            return 'ERROR'
    elif length == 6:
        if 0 <= index < 10:
            return '00000' + str(index)
        elif 10 <= index < 100:
            return '0000' + str(index)
        elif 100 <= index < 1000:
            return '000' + str(index)
        elif 1000 <= index < 10000:
            return '00' + str(index)
        elif 10000 <= index < 100000:
            return '0' + str(index)
        elif 100000 <= index < 1000000:
            return str(index)
        else:
            return 'ERROR'
    else:
        return 'ERROR'
