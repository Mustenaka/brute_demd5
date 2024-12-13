# brute_demd5

# Password MD5 Project

## 项目简介
这是一个完整的 Python 工具项目，包含以下功能：
1. 从原始密码列表生成 MD5 映射文件。
2. 根据给定的 MD5 值快速查找对应的原始字符串。

该项目分为两个主要功能模块：
- **MD5生成模块：** 将字符串生成对应的 MD5 哈希值映射。
- **MD5查找模块：** 从映射文件中查找指定 MD5 值的原始字符串。

---

## 文件说明
### 目录结构 
- **`src/md5_lookup.py`**  
  包含 `MD5Lookup` 类，用于高效查找 MD5 值对应的原始字符串，支持分块加载大文件。

- **`generate_map.py`**  
  包含 `GenerateMap` 类，从密码列表中生成 MD5 映射文件。

- **`src/main.py`**  
  项目入口，通过命令行参数调用 MD5 查找功能。

- **`password_list/`**  
  存放原始密码列表文件，默认读取目录中所有 `.txt` 文件。

- **`md5_mapping.txt`**  
  自动生成的 MD5 映射文件，存储格式为 `MD5\t原始字符串`。

---

## 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/Mustenaka/brute_demd5
```

### 2. 运行
```
python main.py -p md5_mapping.txt 48abc24a5c27f2e32839a9c40268e062
```