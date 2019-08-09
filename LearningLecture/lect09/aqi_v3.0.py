"""
    作者： Michael
    日期： 2／12／2018
    版本： 3。0
    功能： AQI计算
    功能：JSON转换CSV
"""
import json
import csv


def process_json_file(filepath):
    """
        解码json文件
    """
    f = open(filepath, mode='r', encoding='utf-8')
    json_list = json.load(f)
    return json_list


def main():
    """
        主函数
    """
    filepath = input('请输入json文件名称： ')
    json_list = process_json_file(filepath)

    lines = []

    # 列名
    lines.append(list(json_list[0].keys()))
    for things in json_list:
        lines.append(list(things.values()))

    f = open('tings.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)

    for line in lines:
        writer.writerow(line)
    f.close()


if __name__ == '__main__':
    main()




