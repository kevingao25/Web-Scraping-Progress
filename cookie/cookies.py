import requests, json

# If access cookies successfully:
# start commenting

# If not:
# Utilize session object
# Convert cookies to dict then to string
# Using requests.utils.dict_from_cookiejar and json.dumps
# Then save the file in txt
# Not the easiest approach but it works


session = requests.session()
url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

# 如果能读取到cookies文件，执行以下代码，跳过except的代码，不用登录就能发表评论
try:
    cookies_txt = open('cookie.txt', 'r')
    cookies_dict = json.loads(cookies_txt.read())
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    session.cookies = cookies

except FileNotFoundError:
    data = {
        'log': input('请输入你的账号:'),
        'pwd': input('请输入你的密码:'),
        'wp-submit': '登录',
        'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
        'testcookie': '1'
    }
    session.post(url, headers=headers, data=data)

    # Start converting
    # Convert from cookie to dict
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    print(cookies_dict)
    # Convert from dict to string
    cookies_str = json.dumps(cookies_dict)
    print(cookies_str)
    # Write the file
    f = open('cookie.txt', 'w')
    f.write(cookies_str)
    f.close()

# Find the comment-post and copy the url and data
url_1 = "https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php"
# Enter the data of comment
data_1 = {
    'comment': input("What's your comment?\n"),
    'submit': '发表评论',
    'comment_post_ID': '13',
    'comment_parent': '0'
}
# Use requests.post to initiate post request
comment = session.post(url_1, headers=headers, data=data_1)  # op: cookies=cookies
print(comment.status_code)
