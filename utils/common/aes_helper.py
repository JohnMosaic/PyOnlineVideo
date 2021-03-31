# -*- coding: UTF-8 -*-
from Crypto.Cipher import AES


def aes_128_encrypt(byte_array, key, vector):
    encrypted_byte_array = []
    try:
        aes_128 = AES.new(len_2_16(key), AES.MODE_CBC, len_2_16(vector))
        encrypted_byte_array = aes_128.encrypt(byte_array)
    except ValueError:
        encrypted_byte_array.clear()
    return encrypted_byte_array


def aes_128_decrypt(byte_array, key, vector):
    decrypted_byte_array = []
    try:
        aes_128 = AES.new(len_2_16(key), AES.MODE_CBC, len_2_16(vector))
        decrypted_byte_array = aes_128.decrypt(byte_array)
    except ValueError:
        decrypted_byte_array.clear()
    return decrypted_byte_array


def len_2_16(s):
    length = len(s)
    if length > 16:
        return str.encode(s[0:16])
    elif length == 16:
        return str.encode(s)
    else:
        return str.encode(s + '\0' * (16 - length))
