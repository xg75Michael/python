"""
    作者： Michael
    日期： 6／12／2018
    版本： 9。0
    功能： AQI计算
    功能：JSON转换CSV
    功能： 根据输入的文件格式进行相应的操作
    功能： 网络爬虫获取实时获取天气
    功能： 使用bs4来爬网页
    功能： 获取所有城市的aqi
    功能： pandas
"""
import pandas as pd


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print('基本信息')
    print(aqi_data.info())

    print('数据预览')
    print(aqi_data.head())

    # 基本统计
    print('AQI最大值: ', aqi_data['AQI'].max())
    print('AQI最小值: ', aqi_data['AQI'].min())
    print('AQI均值: ', aqi_data['AQI'].mean())

    # top10
    top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
    print('空气质量最好的10个城市： ')
    print(top10_cities)

    # bottom10
    # bottom10_cities = aqi_data.sort_values(by=['AQI']).tail(10)
    bottom10_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print('空气质量最差的10个城市： ')
    print(bottom10_cities)

    # 保存csv文件
    top10_cities.to_csv('top10_aqi.csv', index=False)
    bottom10_cities.to_csv('bottom_aqi.csv', index=False)


if __name__ == '__main__':
    main()




