"""
    作者： Michael Gao
    功能： 52周存钱挑战
    版本： 2。0
    日期： 21／11／2018
    新增： 记录每周的存款数
"""


import math


def main():
    """
        主函数
    """

    money_per_week = 10     # 每周存入的金额
    i = 1                   # 记录周数
    increase_money = 10     # 递增的金额
    total_week = 52         # 总共的周数

    money_list = []         # 记录每周存款数的列表

    while i <= total_week:
        # 存钱操作，放在一个list中
        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # 输出信息
        print('第{}周，存入{}元，账户累计{}元。'.format(i, money_per_week, saving))
        # 更新下一周的存钱金额
        money_per_week += increase_money
        i += 1


if __name__ == '__main__':
    main()




