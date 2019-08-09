"""
    作者： Michael Gao
    功能： 52周存钱挑战
    版本： 4。0
    日期： 22／11／2018
    新增： 使用循环直接计数
    新增： 灵活设置每周的存款数，增加的存款数及存款周数
    新增： 根据用户输入的日期，判断是一年中的第几周， 然后输出相应的存款金额
"""


import math
import datetime

# 全局变量
# saving = 0


def saving_money_in_weeks(money_per_week, increase_money, total_week):

    # global saving
    money_list = []                     # 记录每周存款数的列表
    saved_money_list = []               # 记录每周用户累计

    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)

        # 输出信息
        # print('第{}周，存入{}元，账户累计{}元。'.format(i + 1, money_per_week, saving))
        money_per_week += increase_money

    return saved_money_list


def main():
    """
        主函数
    """

    money_per_week = float(input('请输入每周的存入金额: '))     # 每周存入的金额
    increase_money = float(input('请输入每周的递增金额: '))     # 递增的金额
    total_week = int(input('请输入总共的周数: '))         # 总共的周数

    saved_money_list = saving_money_in_weeks(money_per_week, increase_money, total_week)

    input_data_str = input('请输入日期（yyyy/mm/dd）: ')
    input_date = datetime.datetime.strptime(input_data_str, '%Y/%m/%d')
    week_number = input_date.isocalendar()[1]

    print('第{}周的存款： {}元'.format(week_number, saved_money_list[week_number - 1]))


if __name__ == '__main__':
    main()




