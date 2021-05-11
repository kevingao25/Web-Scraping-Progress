import requests
from bs4 import BeautifulSoup
import random
ip_list = []
proxy=''
def get_ip_list():
    url = 'https://www.xicidaili.com/wt/'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    bs = BeautifulSoup(res.text, 'html.parser')
    results = bs.find('table',id='ip_list').find_all('tr')
    for result in results[1:]:
        ip = result.select('td')[1].text
        port = result.select('td')[2].text
        judge(ip, port)
def judge(ip, port):
    global ip_list
    global proxy
    proxy = {'http': ip+':'+port}
    try:
        res = requests.get('https://www.baidu.com', proxies=proxy)
    except Exception:
        print('该 ip:' + ip + '无效')
        return False
    else:
        if 200 <= res.status_code < 300:
            ip_list.append((ip, port))
            return True
        else:
            print('该 ip:' + ip + '无效')
            return False
def get_random_ip():
    ip, port = random.choice(ip_list)
    #ip_list列表里面的元素是元祖，可以直接赋值
    while True:
        result = judge(ip, port)
        if result:
            return ip + ':' + port
            #遇到return直接结束函数，不需要特地break
        else:
            ip_list.remove((ip, port))
def get_proxy():
    global proxy
    get_ip_list()
    print(len(ip_list))
    proxy = {'http': str(get_random_ip())}
    print(proxy)
get_proxy()
res = requests.get('https://www.baidu.com', proxies=proxy)
print(res.status_code)