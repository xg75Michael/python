"""
    作者： Michael
    日期： 8／12／2018
    版本： 10。0
    功能： AQI计算
    功能：JSON转换CSV
    功能： 根据输入的文件格式进行相应的操作
    功能： 网络爬虫获取实时获取天气
    功能： 使用bs4来爬网页
    功能： 获取所有城市的aqi
    功能： pandas
    功能： pandas数据处理
"""
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
# plt.reParams['font.sans-serif'] = ['SimHei']
# plt.reParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print('基本信息')
    print(aqi_data.info())

    print('数据预览')
    print(aqi_data.head())

    # 数据清洗
    # 只保留AQI > 0 的数据
    # filter_condition = aqi_data['AQI'] > 0
    # clean_aqi_data = aqi_data[filter_condition]

    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    # 基本统计
    print('AQI最大值: ', clean_aqi_data['AQI'].max())
    print('AQI最小值: ', clean_aqi_data['AQI'].min())
    print('AQI均值: ', clean_aqi_data['AQI'].mean())

    # top50
    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='line', x='city', y='AQI', title='Best cities in China', figsize=(10, 5))

    plt.savefig('top50_aqi_bar.png')
    plt.show()


if __name__ == '__main__':
    main()




