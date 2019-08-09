"""
    作者： Michael Gao
    功能： 汇率兑换
    版本： 3.0
    日期： 14 Nov
    新增： 2.0.根据输入判断是人民币还是美元，进行相应的转换计算
          3.0.运行程序可以一直运行，直到用户选择推出
          4.0.将汇率兑换功能封装到函数中
"""


def convert_currency(im, er):
    """
        汇率兑换函数
    """
    out = im * er
    return out


# 美元对应人民币的汇率
USD_VS_RMB = 6.77

# 带单位的货币输入 比如100CNY
currency_str_value = input('请输入带单位的货币金额： ')

# 获取货币单位
unit = currency_str_value[-3:]

if unit == 'CNY':

    exchange_rate = 1 / USD_VS_RMB

elif unit == 'USD':
    exchange_rate = USD_VS_RMB

else:
    exchange_rate = -1

if exchange_rate != -1:
    in_money = eval(currency_str_value[:-3])

    # 调用函数
    out_money = convert_currency(in_money, exchange_rate)
    print('转换后的金额： ', out_money)
else:
    print('不支持该种货币（请输入CNY或USD）！')






