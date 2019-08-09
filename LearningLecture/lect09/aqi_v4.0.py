"""
    作者： Michael
    日期： 4／12／2018
    版本： 4。0
    功能： AQI计算
    功能：JSON转换CSV
    功能： 根据输入的文件格式进行相应的操作
"""
import json
import csv
import os


def process_json_file(filepath):
    """
        解码json文件
    """
    # f = open(filepath, mode='r', encoding='utf-8')
    # json_list = json.load(f)
    # return json_list

    with open(filepath, mode='r', encoding='utf-8') as f:
        json_list = json.load(f)
    print(json_list)


def process_csv_file(filepath):
    """
        解码csv文件
    """
    with open(filepath, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(','.join(row))


def main():
    """
        主函数
    """
    filepath = input('请输入文件名称： ')
    # 把文件名分割
    filename, file_ext = os.path.splitext(filepath)
    if file_ext == '.json':
        # json 文件
        process_json_file(filepath)
    elif file_ext == '.csv':
        # csv 文件
        process_csv_file(filepath)
    else:
        print('不支持该文件格式！')


if __name__ == '__main__':
    main()




