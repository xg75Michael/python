"""
    作者： Michael Gao
    版本： 4。0
    日期： 25／11／2018
    功能： 输入某年某月某日，判断这一天是这一年的第几天？
    新增： Test, 一行代码！
"""
from datetime import datetime


def main():
    print('这是当年的第{}天！'.format((datetime.strptime(input('输入具体时间（yyyy/mm/dd）：'), '%Y/%m/%d')).strftime('%j')))


if __name__ == '__main__':
    main()

