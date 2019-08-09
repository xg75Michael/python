"""
    作者： Michael
    日期： 1／12／2018
    版本： 2。0
    功能： AQI计算
    功能：
"""
import json


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
    json_list.sort(key=lambda city: city['id'])

    print(json_list)


if __name__ == '__main__':
    main()




