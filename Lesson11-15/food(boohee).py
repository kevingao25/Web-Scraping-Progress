from gevent import monkey

monkey.patch_all()
import gevent, requests, bs4, csv
from gevent.queue import Queue

headers = {
    'User-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"}

csv_file = open("food.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)


for x in range(1, 4):
    for i in range(1, 4):
        url = "http://www.boohee.com/food/group/" + str(x) + "?page" + str(i)
        res = requests.get(url, headers=headers)
        bs = bs4.BeautifulSoup(res.text, 'html.parser')
        food = bs.find_all('li', class_="item clearfix")

        for content in food:
            name = content.find("h4").text
            link = 'http://www.boohee.com' + content.find("a")["href"]
            food_calorie = content.find('p').text
            writer.writerow([name, link, food_calorie])
            print(name, link, food_calorie)

csv_file.close()
