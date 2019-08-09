"""
    作者： Michael
    日期： 4／12／2018
    版本： 5。0
    功能： AQI计算
    功能：JSON转换CSV
    功能： 根据输入的文件格式进行相应的操作
    功能： 网络爬虫获取实时获取天气
"""
import requests


def get_html_text(url):
    """
        返回url的文本
    """
    r = requests.get(url, timeout=30)
    print(r.status_code)
    return r.text


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市的拼音： ')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)

    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_value = url_text[begin_index: end_index]
    print('{} 城市的空气质量为: {}'.format(city_pinyin, aqi_value))


if __name__ == '__main__':
    main()




