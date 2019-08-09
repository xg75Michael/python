"""
    作者： Michael
    功能： 模拟掷骰子
    版本： 5.0
    日期： 30／11／2018
    新增： 模拟投掷两个骰子
    新增： 可视化抛掷两个骰子的结果
    新增： 直方图对结果进行简单的数据统计和分析
    新增： 使用科学计算库Numpy简化程序
"""
import numpy as np
import matplotlib.pyplot as plt
# 解决中文显示问题： 给它一个中文字体
# import matplotlib.font_manager as mfm
# font_path = ''
# font_chinese = mfm.FontProperites(fname = font_path)
# plt.text(......, fontproperties = font_chinese)

# 解决中文显示问题--------------------未解决
# plt.rcParams['font.sans-serif'] = ['STKaiti']
# plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    total_times = 1000

    # 记录第一个骰子的结果
    roll1_array = np.random.randint(1, 7, size=total_times)
    roll2_array = np.random.randint(1, 7, size=total_times)
    roll3_array = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_array + roll2_array + roll3_array

    hist, bins = np.histogram(result_arr, bins=range(3, 20))
    print(hist)
    print(bins)

    # 数据可视化
    plt.hist(result_arr, bins=range(2, 20), density=1, edgecolor='black', linewidth=1, rwidth=0.9)

    # 设置坐标轴显示
    tick_lables = ['2points', '3points', '4points', '5points', '6points', '7points', '8points',
                   '9points', '10points', '11points', '12points', '13points', '14points', '15points',
                   '16points', '17points', '18points']
    tick_pos = np.arange(2, 19) + 0.5
    plt.xticks(tick_pos, tick_lables)
    plt.title('Dice Sta')
    plt.xlabel('Rolls')
    plt.ylabel('%')
    plt.show()


if __name__ == '__main__':
        main()

