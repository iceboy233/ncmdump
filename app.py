# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:32:51 2018

@author: Nzix
"""

import argparse, os, sys, re
import ncmdump

parser = argparse.ArgumentParser(
    prog = 'ncmdump'
)
parser.add_argument(
    'input', metavar = 'input', nargs = '*', default = ['.'],
    help = 'ncm file or folder path'
)
parser.add_argument(
    '-f', metavar = 'format', dest = 'format', default = '',
    help = 'customize naming format'
)
parser.add_argument(
    '-o', metavar = 'output', dest = 'output',
    help = 'customize saving folder'
)
parser.add_argument(
    '-d', dest = 'delete', action='store_true',
    help = 'delete source after conversion'
)
args = parser.parse_args()

def validate_name(file_name):
    pattern = {u'\\': u'＼', u'/': u'／', u':': u'：', u'*': u'＊', u'?': u'？', u'"': u'＂', u'<': u'＜', u'>': u'＞', u'|': u'｜'}
    for character in pattern:
        file_name = file_name.replace(character, pattern[character])
    return file_name

def validate_collision(file_path):
    index = 1
    while os.path.exists(file_path):
        file_path = '({})'.format(index).join(os.path.splitext(file_path))
        index += 1
    return file_path

def name_format(path, meta):
    information = {
        'artist': ','.join([artist[0] for artist in meta['artist']]),
        'title': meta['musicName'],
        'album': meta['album']
    }

    def substitute(matched):
        key = matched.group(1)
        if key in information:
            return information[key]
        else:
            return key

    name = re.sub(r'%(.+?)%', substitute, args.format)
    name = os.path.splitext(os.path.split(path)[1])[0] if not name else name
    name = validate_name(name)
    name += '.' + meta['format']
    folder = args.output if args.output else os.path.dirname(path)
    save = os.path.join(folder, name)
    save = validate_collision(save)
    return save

if args.output:
    args.output = os.path.abspath(args.output)
    if not os.path.exists(args.output):
        print('output does not exist')
        exit()
    if not os.path.isdir(args.output):
        print('output is not a folder')
        exit()

files = []
for item in args.input:
    item = os.path.abspath(item)
    if not os.path.exists(item):
        continue
    if os.path.isdir(item):
        files += [os.path.join(item, _file) for _file in os.listdir(item) if os.path.splitext(_file)[-1] == '.ncm']
    else:
        flles += [item]

if sys.version[0] == '2':
    files = [file_name.decode(sys.stdin.encoding) for file_name in files]

if not files:
    print('empty input')
    exit()

for _file in files:
    try:
        _save = ncmdump.dump(_file, name_format)
        print(os.path.split(_save)[-1])
        if args.delete: os.remove(_file)
    except KeyboardInterrupt:
        exit()