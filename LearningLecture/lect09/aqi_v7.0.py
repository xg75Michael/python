"""
    作者： Michael
    日期： 5／12／2018
    版本： 7。0
    功能： AQI计算
    功能：JSON转换CSV
    功能： 根据输入的文件格式进行相应的操作
    功能： 网络爬虫获取实时获取天气
    功能： 使用bs4来爬网页
    功能： 获取所有城市的aqi
"""
import requests
from bs4 import BeautifulSoup as bfs


def get_city_aqi(city_pinyin):
    """
        获取城市的aqi
    """
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout=30)
    soup = bfs(r.text, 'lxml')
    div_list = soup.findAll('div', {'class': 'span1'})

    city_aqi = []

    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()
        city_aqi.append((caption, value))

    return city_aqi


def get_all_cities():
    """
        获取所有城市的url
    """
    url = 'http://pm25.in/'
    city_list = []
    r = requests.get(url, timeout=30)
    soup = bfs(r.text, 'lxml')

    city_div = soup.find_all('div', {'class': 'bottom'})[1]
    city_link_list = city_div.find_all('a')
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href'][1:]
        city_list.append((city_name, city_pinyin))

    return city_list


def main():
    """
        主函数
    """
    city_list = get_all_cities()
    for city in city_list:
        city_name = city[0]
        city_pinyin = city[1]
        city_aqi = get_city_aqi(city_pinyin)
        print(city_name, city_aqi)


if __name__ == '__main__':
    main()




