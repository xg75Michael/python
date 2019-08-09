"""
    作者： Michael Gao
    功能： 汇率兑换
    版本： 3.0
    日期： 14 Nov
    新增： 2.0.根据输入判断是人民币还是美元，进行相应的转换计算
          3.0.运行程序可以一直运行，直到用户选择推出
"""


# 美元对应人民币的汇率
USD_VS_RMB = 6.77



i = 0

# 带单位的货币输入 比如100CNY
currency_str_value = input('请输入带单位的货币金额（退出程序请输入Q）： ')

while currency_str_value != 'Q':
    i = i + 1
    print('循环次数', i)
    # 获取货币单位
    unit = currency_str_value[-3:]

    if unit == 'CNY':
        # 输入的是人民币
        rmb_str_value = currency_str_value[:-3]
        rmb_value = eval(rmb_str_value)
        usd_value = rmb_value / USD_VS_RMB

        print('美元（USD）的金额是： ', usd_value)

    elif unit == 'USD':
        # 输入的是美元
        usd_str_value = currency_str_value[:-3]
        usd_value = eval(usd_str_value)
        rmb_value = usd_value * USD_VS_RMB

        print('人民币（CNY）的金额是： ', rmb_value)

    else:
        # 其他情况
        print('此程序目前版本尚不支持该种', unit, '货币！', '请输入CNY或USD')
    print('***********************************************************')
    currency_str_value = input('请输入带单位的货币金额（退出程序请输入Q）： ')


print('程序已退出！')

