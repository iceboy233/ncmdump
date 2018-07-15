# Netease Cloud Music Copyright Protection File Dump (Python version)

## 简介

早就在算计网易云ncm文件，不过一直没什么机会，前些天突然看到已经有大佬 [anonymous5l/ncmdump ](https://github.com/anonymous5l/ncmdump)实现了，因为好奇加密算法就用Python移植了下，啊大佬不愧是大佬，感激！测试发现转换出来的媒体文件都已包含媒体信息，故未再实现原repo中的写tag操作。还有Python实现比C++慢不少。仅供学习交流，请勿传播扩散。用Python处理字节真让人头大emmm

## 依赖

```
pip(3) install pycrypto
```

## 使用

```
python(3) ncmdump.py [files ...]
```