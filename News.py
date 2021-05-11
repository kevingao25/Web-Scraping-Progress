# 导入模块
import requests

# 定义url，params，headers等变量
url = "https://www.toutiao.com/api/search/content/"

keyword = input("你想要搜索什么?\n")
# count = input("你想要搜索多少条新闻?\n")

for i in range(5):
    offset = str(10 * i)
    params = {'aid': '24', 'app_name': 'web_search', 'offset': offset, 'format': 'json', 'keyword': keyword,
              'autoload': 'true', 'count': '20', 'en_qc': '1',
              'cur_tab': '1', 'from': 'search_tab', 'pd': 'synthesis', 'timestamp': '1597805260196',
              '_signature': 'dtEYPAAgEBCwhqGxqNBu4nbQWSAACnwFpTASKTMh-7VzDcR4ykquvMXl2F.pPxwChz4GKYLO1cUznXPfka5UP0CD1lz0TY6sU7IVp5.oVpcCMmgAAzVbhyv36kQ0P75E0VA'}
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    # 发送请求，并把响应内容赋值到变量res里面
    res = requests.get(url, params=params, headers=headers)

    # 定位数据
    articles = res.json()
    data = articles['data']

    # 遍历列表，提取出里面的新闻标题与链接
    for i in data:
        try:
            list1 = [i['title'], i["article_url"]]
            print(list1)
        except:
            pass


# import requests
# import csv
#
# # 调用open()函数打开csv文件，传入参数：文件名“articles.csv”、写入模式“w”、newline=''。
# csv_file = open('特朗普.csv', 'w', newline='', encoding='utf-8')
# # 用csv.writer()函数创建一个writer对象。
# writer = csv.writer(csv_file)
# # 创建一个列表
# lst = ['新闻标题','链接']
# # 调用writer对象的writerow()方法，可以在csv文件里写入一行文字 “标题”和“链接”和"摘要"。
# writer.writerow(lst)
#
# # 设置headers,url,offset等变量
# headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# url='https://www.toutiao.com/api/search/content/'
# offset=0
#
# # 循环爬取60页头条数据
# while True:
#     if offset < 80:
#         offset += 20
#     else:
#         break
#     params={'aid': '24', 'app_name': 'web_search', 'offset': offset, 'format': 'json', 'keyword': '特朗普：', 'autoload': 'true', 'count': '20', 'en_qc': '1',
# 'cur_tab': '1', 'from': 'search_tab', 'pd': 'synthesis', 'timestamp': '1597805260196', '_signature': 'dtEYPAAgEBCwhqGxqNBu4nbQWSAACnwFpTASKTMh-7VzDcR4ykquvMXl2F.pPxwChz4GKYLO1cUznXPfka5UP0CD1lz0TY6sU7IVp5.oVpcCMmgAAzVbhyv36kQ0P75E0VA'}
#     res=requests.get(url,headers=headers,params=params)
#     articles=res.json()
#     data=articles['data']
#     for i in data:
#         try:
#             list1=[i['title'],i["article_url"]]
#             writer.writerow(list1)
#             print(list1)
#         except:
#             pass
#
# csv_file.close
