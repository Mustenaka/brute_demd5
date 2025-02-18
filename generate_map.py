import os
import hashlib
import base64

from src.framework.Singleton import Singleton
from tqdm import tqdm, trange

class GenerateMap(Singleton):
    _data_loaded = False
    _txt_files = []
    dic_path = ""
    md5_map = {}
    md5_b64_map = {}

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
            md5_b64 = self.md5_to_base64(original_string)

            self.md5_map[original_string] = md5_hash
            self.md5_b64_map[original_string] = md5_b64
            # print(md5_hash + " --- " + original_string)

    def md5_to_base64(self, input_string):
        # 计算 MD5 哈希
        md5_hash = hashlib.md5(input_string.encode('utf-8')).digest()
        
        # 转换为 Base64 编码
        base64_hash = base64.b64encode(md5_hash).decode('utf-8')
        
        base64_hash = base64_hash.replace("=", "")

        return base64_hash

    def save_to_file(self, file_path):
        """
        将MD5和原始字符串的映射关系保存到文件中。

        :param file_path: str, 保存的文件路径
        """
        md5_file_path = file_path + ".txt"
        md5_b64_file_path = file_path + "_b64.txt"

        with open(md5_file_path, 'w', encoding='utf-8') as file:
            for original_string, md5_hash in self.md5_map.items():
                file.write(f"{md5_hash}\t{original_string}\n")
        
        with open(md5_b64_file_path, 'w', encoding='utf-8') as file:
            for original_string, md5_b64 in self.md5_b64_map.items():
                file.write(f"{md5_b64}\t{original_string}\n")


# 示例用法
if __name__ == "__main__":
    gen = GenerateMap(dic_path="password_list")

    # 生成MD5映射
    gen.generate_md5()

    # 保存到文件
    gen.save_to_file("book\md5_mapping")

    print("MD5映射已保存到文件 md5_mapping.txt")
