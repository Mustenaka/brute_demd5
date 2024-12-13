# Brute Demd5

Quickly find the original password corresponding to common MD5 hashes. This is a security tool that supports command-line usage. It comes with a built-in password list, and users can also manually generate their own.

# Password MD5 Project

## Project Overview

This is a complete Python tool project that includes the following features:
1.	Generate MD5 mapping files from a raw password list.
2.	Quickly find the original string corresponding to a given MD5 hash.

The project is divided into two main functional modules:
1. MD5 Generation Module: Generates MD5 hash mappings for strings.
2.  MD5 Lookup Module: Finds the original string corresponding to an MD5 hash from a mapping file.

## File Description

### Directory Structure
- **`src/md5_lookup.py`**  
Contains the MD5Lookup class for efficiently finding the original string corresponding to an MD5 hash. It supports block-based loading of large files.
- **`generate_map.py`**  
Contains the GenerateMap class to generate MD5 mapping files from a password list.
- **`src/main.py`**  
The project entry point, which enables MD5 lookup functionality through command-line arguments.
- **`password_list/`**  
Stores the raw password list files, with all .txt files in this directory being read by default.
- **`md5_mapping.txt`**  
Automatically generated MD5 mapping file, stored in the format MD5\tOriginal String.

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Mustenaka/brute_demd5
```

### 2. Run the Tool
```
python main.py -p md5_mapping.txt 48abc24a5c27f2e32839a9c40268e062
```