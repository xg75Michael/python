import os
from PIL import Image

# 返回当前工作目录
MAX_SIZE = 1024 * 2
CURRENT_PATH = os.getcwd()
IMG_PATH = '\input'
IMG_OUTPUT = '\output'
TARGET_PATH = CURRENT_PATH + IMG_PATH
OUTPUT_PATH = CURRENT_PATH + IMG_OUTPUT

list_dirs = os.walk(TARGET_PATH)
# 转换格式
IMG_EXP = ".webp"

# 获取最高所有文件
for root, dirs_name, files_name in list_dirs:
    for i in files_name:
        file_name = os.path.join(root, i)
        name_only = os.path.splitext(i)[0]
        target_name = name_only + IMG_EXP
        target_file_name = os.path.join(OUTPUT_PATH, target_name)
        img = Image.open(file_name)
        img.save(target_file_name, quality=95)
        print(target_file_name)
print('All Done')
