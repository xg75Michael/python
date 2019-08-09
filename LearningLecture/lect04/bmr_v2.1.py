"""
    作者： Michael Gao
    功能： BMR计算
    版本： 2。1
    日期： 19／11／2018
    新增： 选择退出循环放在主函数后
"""


def main():
    """
        主函数
    """

    # 性别
    gender = input('性别： ')

    # 体重
    weight = float(input('体重（kg）： '))

    # 身高
    height = float(input('身高（cm）： '))

    # 年龄
    age = int(input('年龄： '))

    if gender == '男':
        # 男性
        bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
    elif gender == '女':
        # 女性
        bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
    else:
        bmr = -1

    if bmr != -1:
        print('基础代谢率： ', bmr, '（大卡）')
    else:
        print('暂不支持该性别！')


if __name__ == '__main__':
    main()
y_or_n = input('请选择是否退出程序（y/n）？')
while y_or_n != 'y':
    main()
    print()  # 输入空行
    y_or_n = input('请选择是否退出程序（y/n）？')
print('程序已退出！')


