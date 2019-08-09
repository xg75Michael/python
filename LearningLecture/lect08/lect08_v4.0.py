"""
    作者： Michael
    功能： 模拟掷骰子
    版本： 4.0
    日期： 30／11／2018
    新增： 模拟投掷两个骰子
    新增： 可视化抛掷两个骰子的结果
    新增： 直方图对结果进行简单的数据统计和分析
"""
import random
import matplotlib.pyplot as plt

# 解决中文显示问题： 给它一个中文字体
# import matplotlib.font_manager as mfm
# font_path = ''
# font_chinese = mfm.FontProperites(fname = font_path)
# plt.text(......, fontproperties = font_chinese)

# 解决中文显示问题--------------------未解决
# plt.rcParams['font.sans-serif'] = ['STKaiti']
# plt.rcParams['axes.unicode_minus'] = False


def roll_dice():
    """
        模拟掷骰子
    """
    roll = random.randint(1, 6)
    return roll


def main():
    """
        主函数
    """
    total_times = 100

    # 记录第一个骰子的结果
    roll_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll_list.append(roll1 + roll2)
    # 数据可视化
    plt.hist(roll_list, bins=range(2, 14), density=1, edgecolor='black', linewidth=1)
    plt.title('Dice Sta')
    plt.xlabel('Rolls')
    plt.ylabel('%')
    plt.show()
    # print(plt.rcParams['font.sans-serif'])


if __name__ == '__main__':
        main()

