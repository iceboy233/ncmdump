# Netease Cloud Music Copyright Protection File Dump

![shield](https://img.shields.io/badge/python-2.7%7C3.4+-blue.svg)

## 简介

感谢大佬的 [anonymous5l/ncmdump ](https://github.com/anonymous5l/ncmdump)项目，因好奇加密算法就用 python 移植了下。自测发现转换出来的媒体文件都已包含媒体信息(包括专辑封面)，~~故未再实现原 repo 中的写 tag 操作~~，应 [issue #1](https://github.com/nondanee/ncmdump/issues/1) 要求补上了写 tag 操作。相比 C++ 实现，此版 python 实现慢不少 (瓶颈在异或操作)，实用性不大，善用左上角搜索寻求其它版本。仅供学习交流，**请勿传播扩散**。

## Fork

- [JamieDummy/NCM_dump](https://github.com/JamieDummy/NCM_dump): 增加 GUI

- [mnilzg/ncmdump](https://github.com/mnilzg/ncmdump): 使用 numpy 大幅提高性能 


## 依赖

```
$ pip install pycryptodome mutagen
```

## 使用

### 指定文件

```
$ python ncmdump.py [files ...]
```
### 遍历工作目录

```
$ python ncmdump.py
```
### 更多选项
```
$ python app.py -h
usage: ncmdump [-h] [-f format] [-o output] [-d] [input [input ...]]

positional arguments:
  input       ncm file or folder path

optional arguments:
  -h, --help  show this help message and exit
  -f format   customize naming format
  -o output   customize saving folder
  -d          delete source after conversion
```

> 自定义命名参数: %artist%, %title%, %album%

