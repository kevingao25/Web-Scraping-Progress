import requests
from bs4 import BeautifulSoup

res = requests.get("http://books.toscrape.com/")
webpage = BeautifulSoup(res.text, 'html.parser')
list_books = webpage.find_all(class_='product_pod')

for tag_books in list_books:
    tag_name = tag_books.find('h3').find('a')
    print(tag_name['title'])
    tag_rating = tag_books.find('p', class_='star-rating')
    print("Star Rating:", tag_rating['class'][1])
    tag_price = tag_books.find('p', class_="price_color")
    print('Price:', tag_price.text, end='\n'+'------------'+"\n")




# # 爬取书店种类
# categories = webpage.find('div', class_="side_categories").find('ul').find_all('li')
#
# for category in categories:
#     tag_name = category.find('a')
#     print(tag_name.text.strip())

