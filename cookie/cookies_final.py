import requests, json

# This is the final version of commenting through cookies and sessions access
# Add the feature of detecting cookies expiring

session = requests.session()
url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def read_cookies():
    cookies_txt = open("cookie.txt", "r")
    cookies_dict = json.loads(cookies_txt.read())
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    session.cookies = cookies
    return


def sign_in():
    data = {
        'log': input('请输入你的账号:'),
        'pwd': input('请输入你的密码:'),
        'wp-submit': '登录',
        'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
        'testcookie': '1'
    }

    session.post(url, headers=headers, data=data)
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    cookies_str = json.dumps(cookies_dict)
    # Write cookies to file
    f = open('cookie.txt', 'w')
    f.write(cookies_str)
    f.close()
    return


def write_message():
    url_1 = "https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php"
    # Enter the data of comment
    data_1 = {
        'comment': input("请输入你要发表的评论："),
        'submit': '发表评论',
        'comment_post_ID': '13',
        'comment_parent': '0'
    }
    comment = session.post(url_1, headers=headers, data=data_1)  # op: cookies=cookies
    return (comment.status_code)


def check_success():
    result = write_message()
    if result == 200:
        print("Comment success!")
        return
    else:
        print("Comment failed, please sign in again.")
        sign_in()
        check_success()


try:
    read_cookies()
except FileNotFoundError:
    sign_in()

check_success()
