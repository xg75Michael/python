"""
    作者： Michael Gao
    功能： 52周存钱挑战
    版本： 4。0
    日期： 22／11／2018
    新增： 使用循环直接计数
    新增： 灵活设置每周的存款数，增加的存款数及存款周数
"""


import math

# 全局变量
# saving = 0


def saving_money_in_weeks(money_per_week, increase_money, total_week):

    # global saving
    money_list = []  # 记录每周存款数的列表
    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # 输出信息
        # print('第{}周，存入{}元，账户累计{}元。'.format(i + 1, money_per_week, saving))
        money_per_week += increase_money

    return saving


def main():
    """
        主函数
    """

    money_per_week = float(input('请输入每周的存入金额: '))     # 每周存入的金额
    increase_money = float(input('请输入每周的递增金额: '))     # 递增的金额
    total_week = int(input('请输入总共的周数: '))         # 总共的周数

    saving = saving_money_in_weeks(money_per_week, increase_money, total_week)
    print('总共存款的金额: ', saving)


if __name__ == '__main__':
    main()




