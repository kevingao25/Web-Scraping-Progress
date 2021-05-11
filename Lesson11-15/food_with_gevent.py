from gevent import monkey

monkey.patch_all()
import gevent, requests, bs4, csv
from gevent.queue import Queue

headers = {
    'User-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"}

csv_file = open("food.csv", 'w', newline='')
writer = csv.writer(csv_file)
work = Queue()

# It's easier to use the format method to get url
url_1 = 'http://www.boohee.com/food/group/{type}?page={page}'
for x in range(1, 4):
    for i in range(1, 4):
        real_url = url_1.format(type=x, page=i)
        work.put_nowait(real_url)


# 第11个常见食物分类的前3页的食物记录的网址：
url_2 = 'http://www.boohee.com/food/view_menu?page={page}'
for x in range(1, 4):
    real_url = url_2.format(page=x)
    work.put_nowait(real_url)
# 通过for循环，能设置第11个常见食物分类的食物的页数。
# 然后，把构造好的网址用put_nowait添加进队

def crawler():
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url, headers=headers)
        bs_res = bs4.BeautifulSoup(res.text, 'html.parser')
        foods = bs_res.find_all('li', class_='item clearfix')

        for content in foods:
            name = content.find_all('a')[1]['title']
            link = 'http://www.boohee.com' + content.find_all("a")[1]["href"]
            food_calorie = content.find('p').text
            writer.writerow([name, link, food_calorie])
            print(name, link, food_calorie)

task_list = []
# Create 5 web crawlers
for x in range(5):
    task = gevent.spawn(crawler())
    task_list.append(task)
gevent.joinall(task_list)

csv_file.close()