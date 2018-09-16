# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 01:05:58 2018

@author: Nzix
"""

import binascii
import struct
import base64
import json
import os
import re
from Crypto.Cipher import AES
from mutagen import mp3, flac, id3


# 文件名有效化函数，用于移除曲名中特殊字符从而成功创建文件
def validate_title(title):
    special_char = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(special_char, "_", title)  # 替换为下划线
    return new_title

# 网易云音乐获取的文件若存在重名情况，一般在文件名后加"(X)"，X为数字
#
def validate_collision(filename):
    start_num = 1
    ori_filename_no_ext = os.path.splitext(filename)[0]
    ori_file_ext = os.path.splitext(filename)[-1]
    while os.path.exists(filename):
        filename = ori_filename_no_ext + '(' + str(start_num) + ')' + ori_file_ext
        start_num = start_num + 1
    return filename


def dump(file_path):

    core_key = binascii.a2b_hex("687A4852416D736F356B496E62617857")
    meta_key = binascii.a2b_hex("2331346C6A6B5F215C5D2630553C2728")
    unpad = lambda s : s[0:-(s[-1] if type(s[-1]) == int else ord(s[-1]))]

    f = open(file_path,'rb')

    # magic header
    header = f.read(8)
    assert binascii.b2a_hex(header) == b'4354454e4644414d'

    # key data
    f.seek(2, 1)
    key_length = f.read(4)
    key_length = struct.unpack('<I', bytes(key_length))[0]

    key_data = bytearray(f.read(key_length))
    key_data = bytes(bytearray([byte ^ 0x64 for byte in key_data]))

    cryptor = AES.new(core_key, AES.MODE_ECB)
    key_data = unpad(cryptor.decrypt(key_data))[17:]
    key_length = len(key_data)

    # key box
    key_data = bytearray(key_data)
    key_box = bytearray(range(256))
    j = 0

    for i in range(256):
        j = (key_box[i] + j + key_data[i % key_length]) & 0xff
        key_box[i], key_box[j] = key_box[j], key_box[i]

    # meta data
    meta_length = f.read(4)
    meta_length = struct.unpack('<I', bytes(meta_length))[0]

    meta_data = bytearray(f.read(meta_length))
    meta_data = bytes(bytearray([byte ^ 0x63 for byte in meta_data]))
    meta_data = base64.b64decode(meta_data[22:])

    cryptor = AES.new(meta_key, AES.MODE_ECB)
    meta_data = unpad(cryptor.decrypt(meta_data)).decode('utf-8')[6:]
    meta_data = json.loads(meta_data)

    # crc32
    crc32 = f.read(4)
    crc32 = struct.unpack('<I', bytes(crc32))[0]

    # album cover
    f.seek(5, 1)
    image_size = f.read(4)
    image_size = struct.unpack('<I', bytes(image_size))[0]
    image_data = f.read(image_size)

    # media data
    # Need to remove special characters in meta_data['musicName'] to make a valid filename
    file_name = validate_title(meta_data['artist'][0][0] + ' - ' + meta_data['musicName'] + '.' + meta_data['format'])
    # Try if there already a file with same name, if so, modify current filename
    file_name = validate_collision(file_name)

    music_path = os.path.join(os.path.split(file_path)[0],file_name)
    m = open(music_path,'wb')

    while True:
        chunk = bytearray(f.read(0x8000))
        chunk_length = len(chunk)
        if not chunk:
            break

        for i in range(chunk_length):
            j = (i + 1) & 0xff
            chunk[i] ^= key_box[(key_box[j] + key_box[(key_box[j] + j) & 0xff]) & 0xff]

        m.write(chunk)

    m.close()
    f.close()

    # media tag
    if meta_data['format'] == 'flac':
        audio = flac.FLAC(music_path)
        # audio.delete()
        image = flac.Picture()
        image.type = 3
        image.mime = 'image/jpeg'
        image.data = image_data
        audio.clear_pictures()
        audio.add_picture(image)
    elif meta_data['format'] == 'mp3':
        audio = mp3.MP3(music_path)
        # audio.delete()
        image = id3.APIC()
        image.type = 3
        image.mime = 'image/jpeg'
        image.data = image_data
        audio.tags.add(image)
        audio.save()
        audio = mp3.EasyMP3(music_path)

    audio['title'] = meta_data['musicName']
    audio['album'] = meta_data['album']
    audio['artist'] = '/'.join([artist[0] for artist in meta_data['artist']])
    audio.save()

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        files = [file_name for file_name in os.listdir('.') if os.path.splitext(file_name)[-1] == '.ncm']
        # 逆序一下防止python将XXX(1)放在XXX之前，导致dump出文件不对应
        files.reverse()

    if not files:
        print('please input file path!')
        
    for file_name in files:
        try:
            dump(file_name)
            print(os.path.split(file_name)[-1])
        except Exception as e:
            print(e)
            pass
        
