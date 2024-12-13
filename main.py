import argparse
from src.Md5Lookup import MD5Lookup

def main():
    """
    主函数，用于通过命令行调用MD5查找工具。
    """
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="根据MD5哈希值查找对应的字符串。")
    parser.add_argument("-p", "--path", required=True, help="映射文件的路径")
    parser.add_argument("md5_hash", help="要查找的MD5哈希值")
    
    # 解析参数
    args = parser.parse_args()
    file_path = args.path
    md5_hash = args.md5_hash

    # 调用MD5查找工具
    lookup = MD5Lookup(file_path=file_path)
    try:
        result = lookup.find_string_by_md5(md5_hash)
        if result:
            print(f"Find Target: {result}")
        else:
            print("Cannot find target")
    except Exception as e:
        print(f"发生错误：{e}")


if __name__ == "__main__":
    main()