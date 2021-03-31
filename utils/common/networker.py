# -*- coding: UTF-8 -*-
import requests


def download_file_2_byte_array(url):
    byte_array = []
    i = 0
    while i < 10:
        try:
            req = requests.get(url)
            byte_array = req.content
            if byte_array:
                break
            else:
                i += 1
        except requests.RequestException:
            byte_array.clear()
            i += 1
    return byte_array


def write_byte_array_2_file(byte_array, filename):
    try:
        with open(filename, mode='wb') as f:
            f.write(byte_array)
        return True
    except IOError:
        return False
