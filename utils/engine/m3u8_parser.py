# -*- coding: UTF-8 -*-
from utils.common.file_operator import record_log


def get_url_array_from_m3u8_file(url_left_part, m3u8_file, mode):
    f = open(m3u8_file, mode='r', encoding='utf8')
    url_dict = {}
    try:
        print('[INFO] Mode ' + str(mode) + ' is parsing m3u8 file.')
        sn = 0
        while True:
            line = f.readline().strip()
            if not line:
                break
            elif '.ts' in line:
                url_dict[sn] = url_left_part + line
                sn += 1
    except IOError as ex:
        print('[ERROR] Mode ' + str(mode) + ' parse error: ' + ex + ' Parse m3u8 file failed...')
        record_log(
            'ERROR',
            'Mode ' + str(mode) + ' parse error: ' + ex,
            'Parse m3u8 file'
        )
    finally:
        if f:
            f.close()
    return url_dict


def get_url_array_from_log_file(log_file, mode):
    f = open(log_file, mode='r', encoding='utf8')
    url_dict = {}
    try:
        print('[INFO] Mode ' + str(mode) + ' is parsing log file.')
        while True:
            line = f.readline().strip()
            if not line:
                break
            elif '#' in line and '>' in line and '.ts' in line:
                tmp = line[line.find('#') + 1:]
                index_str = tmp[0:tmp.find('>')]
                url = tmp[tmp.find('>') + 1:tmp.find('.ts') - tmp.find('>') + 2]
                if index_str not in url_dict.keys():
                    url_dict[index_str] = url
    except IOError as ex:
        print('[ERROR] Mode ' + str(mode) + ' parse error: ' + ex + ' Parse log file failed...')
        record_log(
            'ERROR',
            'Mode ' + str(mode) + ' parse error: ' + ex,
            'Parse log file'
        )
    finally:
        if f:
            f.close()
    return url_dict
