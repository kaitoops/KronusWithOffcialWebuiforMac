import os
import zipfile
from pathlib import Path

def create_zip_package():
    """创建ZIP压缩包"""
    print("创建ZIP压缩包...")
    
    # 源目录
    source_dir = r"G:\GitHubcodecollection\kronosWithOfficalWebuiForMac\kronos_mac_installation_package"
    # 目标ZIP文件
    zip_file = r"G:\GitHubcodecollection\kronosWithOfficalWebuiForMac\kronos_mac_installation_package.zip"
    
    # 创建ZIP文件
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 遍历目录树
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # 计算在ZIP中的相对路径
                arc_path = os.path.relpath(file_path, os.path.dirname(source_dir))
                zipf.write(file_path, arc_path)
                print(f"添加文件: {arc_path}")
    
    print(f"ZIP压缩包创建完成: {zip_file}")
    # 获取文件大小
    file_size = os.path.getsize(zip_file)
    print(f"文件大小: {file_size / (1024*1024):.2f} MB")

if __name__ == "__main__":
    create_zip_package()