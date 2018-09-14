# Netease Cloud Music Copyright Protection File Dump (Python version)

## 简介

感激大佬的 [anonymous5l/ncmdump ](https://github.com/anonymous5l/ncmdump)项目，因好奇加密算法就用Python移植了下。自测发现转换出来的媒体文件都已包含媒体信息(包括专辑封面)，~~故未再实现原repo中的写tag操作~~，应issue要求还是补上了写tag操作。Python实现比C++慢不少，实用性不大，仅供学习交流，请勿传播扩散。
## 依赖

```
pip(3) install pycryptodome mutagen
```

## 使用

指定ncm文件
```
python(3) ncmdump.py [files ...]
```
工作目录下所有ncm文件
```
python(3) ncmdump.py
```