import os

class MD5Lookup:
    def __init__(self, file_path, chunk_size=1024 * 1024):
        """
        初始化MD5查找工具。
        :param file_path: 文档路径
        :param chunk_size: 每次读取的块大小（字节），默认1MB
        """
        self.file_path = file_path
        self.chunk_size = chunk_size

    def find_string_by_md5(self, md5_hash):
        """
        根据MD5哈希值查找对应的字符串。
        :param md5_hash: 输入的MD5字符串
        :return: 对应的字符串，未找到时返回None
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File {self.file_path} does not exist.")
        
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                while True:
                    lines = file.readlines(self.chunk_size)
                    if not lines:
                        break
                    
                    for line in lines:
                        parts = line.strip().split("\t")
                        if len(parts) == 2 and parts[0] == md5_hash:
                            return parts[1]
        except Exception as e:
            raise RuntimeError(f"Error reading file: {e}")
        
        return None


# 示例使用
if __name__ == "__main__":
    # 初始化工具类，指定文件路径
    lookup = MD5Lookup(file_path="/Users/andrew/Projects/PythonProjects/Tools/brute_demd5/md5_mapping.txt")
    
    # 输入MD5哈希值
    input_md5 = "48abc24a5c27f2e32839a9c40268e062"
    
    # 查找并输出结果
    result = lookup.find_string_by_md5(input_md5)
    if result:
        print(f"找到对应字符串：{result}")
    else:
        print("未找到对应的字符串。")