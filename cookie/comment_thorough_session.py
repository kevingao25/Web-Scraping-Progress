import requests

# You can send a comment through either cookies or session
# Cookies and sessions are related to each other


# Create Session object
session = requests.session()
# Import URL
url = "https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php"
# Add headers
header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}
# Add data header with account and pwd
data = {
    'log': 'forchangeman',
    'pwd': 'forchange123',
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': '1'
}

session.post(url,headers=header,data=data)
# # Use requests.post to login
# login_in = requests.post(url, headers=header, data=data)
# # Use the cookies method
# cookies = login_in.cookies
# print(login_in)

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
comment = session.post(url_1, headers=header, data=data_1)     # op: cookies=cookies
print(comment)
