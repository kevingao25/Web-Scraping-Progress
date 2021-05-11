import requests

# Search url
url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp"

# Include headers
raw_headers = '''origin: https://y.qq.com
referer: https://y.qq.com/portal/search.html
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'''
headers = dict([line.split(": ", 1) for line in raw_headers.split("\n")])
print(headers)

for x in range(5):
    params = {
        "ct": "24",
        "qqmusic_ver": "1298",
        "remoteplace": "txt.yqq.lyric",
        "searchid": "95492799682216143",
        "aggr": "0",
        "catZhida": "1",
        "lossless": "0",
        "sem": "1",
        "t": "7",
        "p": str(x+1),
        "n": "5",
        "w": "周杰伦",
        "g_tk_new_20200303": "5381",
        "g_tk": "5381",
        "loginUin": "0",
        "hostUin": "0",
        "format": "json",
        "inCharset": "utf8",
        "outCharset": "utf - 8",
        "notice": "0",
        "platform": "yqq.json",
        "needNewCode": "0"}

    res = requests.get(url, headers=headers, params=params)
    json_music = res.json()
    list_music = json_music['data']['lyric']['list']
    for song in list_music:
        print("Song name: ", song['songname'])
        print("Album name: ", song['albumname'])
        print("Streaming url: ", 'https://y.qq.com/n/yqq/song/' + song['songmid'] + '.html')
        print("--------------------------------------------------------------------")
        
