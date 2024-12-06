import hashlib

class FileHashGenerator:
    def __init__(self, file_path):
        """
        初始化类，接受文件路径。

        :param file_path: str, 文件的路径
        """
        self.file_path = file_path

    def calculate_hash(self, algorithm):
        """
        根据指定的哈希算法计算文件的校验值。

        :param algorithm: str, 哈希算法名称 ('md5', 'sha1', etc.)
        :return: str, 文件的哈希值
        """
        hash_func = hashlib.new(algorithm)
        
        with open(self.file_path, 'rb') as file:
            while chunk := file.read(8192):
                hash_func.update(chunk)

        return hash_func.hexdigest()

    def generate_file_hashes(self, output_file):
        """
        生成文件的 MD5 和 SHA1 哈希，并保存到指定文件中。

        :param output_file: str, 输出文件路径
        """
        md5_hash = self.calculate_hash('md5')
        sha1_hash = self.calculate_hash('sha1')

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"File: {self.file_path}\n")
            file.write(f"MD5: {md5_hash}\n")
            file.write(f"SHA1: {sha1_hash}\n")

# 示例用法
if __name__ == "__main__":
    # 输入的文件路径
    file_path = "example.txt"

    # 创建FileHashGenerator实例
    hash_generator = FileHashGenerator(file_path)

    # 生成哈希值并保存到文件
    hash_generator.generate_file_hashes("file_hashes.txt")

    print("文件哈希信息已保存到 file_hashes.txt")
