# Netease Cloud Music Copyright Protection File Dump

![shield](https://img.shields.io/badge/python-2.7%7C3.4+-blue.svg)

## About

感谢大佬的 [anonymous5l/ncmdump](https://github.com/anonymous5l/ncmdump) 项目，因好奇加密算法就用 python 移植了下。仅供学习交流，**请勿传播扩散**。

## Fork

- [JamieDummy/NCM_dump](https://github.com/JamieDummy/NCM_dump): 增加 GUI
- [mnilzg/ncmdump](https://github.com/mnilzg/ncmdump): 使用 numpy 大幅提高性能 


## Dependency

```
$ pip install pycryptodome mutagen
```

## Usage

### Specify files

```
$ python ncmdump.py [file ...]
```
### Traverse working directory

```
$ python ncmdump.py
```
### More options
```
$ python app.py -h
usage: ncmdump [-h] [-f format] [-o output] [-d] [-c | -s] [input [input ...]]

positional arguments:
  input       ncm file or folder path

optional arguments:
  -h, --help  show this help message and exit
  -f format   customize naming format
  -o output   customize saving folder
  -d          delete source after conversion
  -c          overwrite file with the same name
  -s          skip conversion if file exist
```

> supported name holder: %artist%, %title%, %album%

