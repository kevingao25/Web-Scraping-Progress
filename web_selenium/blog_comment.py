#pwd: Wrrqjz6rp@@J0@H#
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
time.sleep(1)

account = driver.find_element_by_id('user_login')
account.send_keys('kevinmingjiang@gmail.com')
pwd = driver.find_element_by_id('user_pass')
pwd.send_keys('Wrrqjz6rp@@J0@H#')
button = driver.find_element_by_name('wp-submit')
button.click()
time.sleep(2)

driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_03/')
time.sleep(2)
comment = driver.find_element_by_id('comment')
comment.send_keys('欧拉欧拉欧拉 selenium')
submit = driver.find_element_by_id('submit')
submit.click()
time.sleep(5)

driver.close()

