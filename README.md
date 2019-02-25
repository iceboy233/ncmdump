# Netease Cloud Music Copyright Protection File Dump

![shield](https://img.shields.io/badge/python-2.7%7C3.4+-blue.svg)

## Thank

- [anonymous5l/ncmdump](https://github.com/anonymous5l/ncmdump): Original repository

## Fork

- [JamieDummy/NCM_dump](https://github.com/JamieDummy/NCM_dump): Add GUI
- [mnilzg/ncmdump](https://github.com/mnilzg/ncmdump): Speed up with NumPy


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

> Supported name holder: %artist%, %title%, %album%

