from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://baijiahao.baidu.com/s?id=1602963250775465697&wfr=spider&for=pc')
time.sleep(1)

web_link = driver.find_element_by_partial_link_text('一拳超人2')
string_url = web_link.get_attribute("href")
print(string_url)

driver.close()