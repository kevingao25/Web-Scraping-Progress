# 本地Chrome浏览器设置方法
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://learn.uwaterloo.ca/d2l/home')
# time.sleep(10)

account = driver.find_element_by_id('userNameInput')
account.send_keys('k27gao@uwaterloo.ca')
next = driver.find_element_by_id('nextButton')
next.click()

pwd = driver.find_element_by_id('passwordInput')
pwd.send_keys('bK#!4QreNS8sq_H')
next = driver.find_element_by_id('submitButton')
next.click()
#
#
# driver.close() # 关闭浏览器