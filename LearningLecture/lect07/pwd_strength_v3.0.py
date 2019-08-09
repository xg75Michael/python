"""
    作者： Michael Gao
    功能： 判断密码强度
    版本： 3.0
    日期： 26／11／2018
    新增： 限制密码设置次数；循环的终止。
    新增： 保存密码及强度到文件中
"""


def check_number_exist(password_str):
    """
        判断字符串中是否含有数字
    """
    has_number = False
    for c in password_str:
        if c.isnumeric():
            has_number = True
            break

    return has_number


def check_letter_exist(password_str):
    """
        判断字符串中是否含有字母
    """
    has_letter = False
    for c in password_str:
        if c.isalpha():
            has_letter = True
            break
    return has_letter


def main():
    """
        主函数
    """

    try_times = 5
    while try_times > 0:

        password = input('请输入密码： ')

        # 密码强度变量
        strength_level = 0

        # 规则一： 密码长度大于等于8
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码要求至少8位！')

        # 规则二： 密码包含数字
        if check_number_exist(password):
            strength_level += 1
        else:
            print('密码要求包含数字！')

        # 规则三： 密码包含字母
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('密码要求包含字母！')

        if strength_level == 0:
            strength = '弱'
        if strength_level == 1:
            strength = '较弱'
        if strength_level == 2:
            strength = '强'
        if strength_level == 3:
            strength = '很强'

        # 把输入的密码写入文件中
        f = open('password_v3.0.txt', 'a')
        f.write('密码: {}, 强度： {}。\n'.format(password, strength))
        f.close()

        if strength_level == 3:
            print('恭喜恭喜，密码强度合格！')
            break

        if strength_level != 3:
            print('恭喜恭喜，密码强度不不不不合格！')
            try_times -= 1
        print()

    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')


if __name__ == '__main__':
    main()



