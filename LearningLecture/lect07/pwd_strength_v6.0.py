"""
    作者： Michael Gao
    功能： 判断密码强度
    版本： 6.0
    日期： 28／11／2018
    新增： 限制密码设置次数；循环的终止。
    新增： 保存密码及强度到文件中
    新增： 读取文件中的密码
    新增： 定义一个password工具类
    新增： 定义一个文件工具类
"""


class PasswordTool:
    """
        密码工具类
    """
    def __init__(self, password):
        # 类的属性
        self.password = password
        self.strength_level = 0

    def process_password(self):
        # 规则一： 密码长度大于等于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码要求至少8位！')

        # 规则二： 密码包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字！')

        # 规则三： 密码包含字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母！')

    # 类的方法
    def check_number_exist(self):
        """
            判断字符串中是否含有数字
        """
        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        """
            判断字符串中是否含有字母
        """
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter


class FileTool:
    """
        文件工具类
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    """
        主函数
    """

    try_times = 5
    file_path = 'password_v6.0.txt'
    # 实例化文件工具对象
    file_tool = FileTool(file_path)

    while try_times > 0:

        password = input('请输入密码： ')

        # 实例化密码工具对象
        password_tool = PasswordTool(password)
        password_tool.process_password()

        line = '密码: {}, 强度： {}。\n'.format(password, password_tool.strength_level)
        # 写操作
        file_tool.write_to_file(line)

        if password_tool.strength_level == 3:
            print('恭喜恭喜，密码强度合格！')
            break

        if password_tool.strength_level != 3:
            print('抱歉抱歉，密码强度不不不不合格！')
            try_times -= 1
        print()

    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')

    # 读操作
    lines = file_tool.read_from_file()
    print(lines)


if __name__ == '__main__':
    main()



