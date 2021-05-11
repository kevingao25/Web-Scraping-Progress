from gevent import monkey

monkey.patch_all()
import gevent, csv, bs4, requests
from gevent.queue import Queue

url = "http://www.mtime.com/top/tv/top100/"
work = Queue()
work.put_nowait(url)

url_2 = "http://www.mtime.com/top/tv/top100/index-{page}.html"
for x in range(1, 11):
    real_url = url_2.format(page=x)
    work.put_nowait(real_url)


def crawler():
    headers = {
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"}
    while not work.empty():
        url = work.get_nowait()
        r = requests.get(url)
        bs_res = bs4.BeautifulSoup(r.text, 'html.parser')
        datas = bs_res.find_all('div', class_="mov_con")
        for data in datas:
            title = data.find("a").text
            data = data.find_all('P')
            TV_data = ''
            for i in data:
                TV_data = TV_data + '' + i.text
            writer.writerow([title, TV_data])
            print([title, TV_data])


csv_file = open('timetop.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)

task_list = []
for x in range(3):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)
