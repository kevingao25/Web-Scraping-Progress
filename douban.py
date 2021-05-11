import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Douban'

sheet['A1'] = '序号'
sheet['B1'] = '电影名'
sheet['C1'] = '评分'
sheet['D1'] = '推荐语'
sheet['E1'] = '链接'

# Requests info from server
headers = {
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x * 25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = BeautifulSoup(res.text, 'html.parser')
    movie_list = bs.find('ol', class_="grid_view").find_all("li")

    # 单独处理movie list
    for movie in movie_list:
        num = movie.find('em').text
        title = movie.find('span', class_='title').text
        rating = movie.find('span', class_='rating_num').text
        url_movie = movie.find('a')['href']
        try:
            comment = movie.find('span', class_='inq').text
        except:
            comment = '评语不存在的'
        sheet.append([num, title, rating, comment, url_movie])

wb.save('douban.xlsx')
