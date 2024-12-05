import os
import hashlib

from src.framework.Singleton import Singleton
from tqdm import tqdm, trange

class GenerateMap(Singleton):
    _data_loaded = False
    _txt_files = []
    dic_path = ""
    md5_map = {}

    def __init__(self, dic_path):
        if not self._data_loaded:
            self.dic_path = dic_path
            self._load_txt_files(dic_path)
            self._data_loaded = True
            self.md5_map = {}

    def _load_txt_files(self, dic_path):
        """
        读取原始密码本文件
        """
        for root, dirs, files in os.walk(dic_path):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        # self._txt_files.extend(f.readlines())
                        for line in f:
                            self._txt_files.append(line.strip())

    def generate_md5(self):
        """
        为字符串列表生成MD5映射。
        """
        # tbar = tqdm(self._txt_files) # 别用这玩意了，性能特别差
        for original_string in self._txt_files:
            # tbar.set_description('Processing' + original_string)
            md5_hash = hashlib.md5(original_string.encode('utf-8')).hexdigest()
            self.md5_map[original_string] = md5_hash
            # print(md5_hash + " --- " + original_string)

    def save_to_file(self, file_path):
        """
        将MD5和原始字符串的映射关系保存到文件中。

        :param file_path: str, 保存的文件路径
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            for original_string, md5_hash in self.md5_map.items():
                file.write(f"{md5_hash}\t{original_string}\n")


# 示例用法
if __name__ == "__main__":
    gen = GenerateMap(dic_path="password_list")

    # 生成MD5映射
    gen.generate_md5()

    # 保存到文件
    gen.save_to_file("md5_mapping.txt")

    print("MD5映射已保存到文件 md5_mapping.txt")
