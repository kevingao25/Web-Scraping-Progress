# 本地Chrome浏览器设置方法
from selenium import  webdriver
import time

# # 本地Chrome浏览器的静默模式设置：
# from selenium import  webdriver #从selenium库中调用webdriver模块
# from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
#
# chrome_options = Options() # 实例化Option对象
# chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
# driver = webdriver.Chrome(options = chrome_options) # 设置引擎为Chrome，在后台默默运行


driver = webdriver.Chrome()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)



teacher = driver.find_element_by_id('teacher')
teacher.send_keys('必须是吴枫呀')
assistant = driver.find_element_by_name('assistant')
assistant.send_keys('都喜欢')
button = driver.find_element_by_class_name('sub')
button.click()
time.sleep(1)
driver.close()

# driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
# time.sleep(2) # 等待两秒，等浏览器加缓冲载数据
#
# pageSource = driver.page_source # 获取完整渲染的网页源代码
# print("The pageSource type is : ", type(pageSource)) # 打印pageSource的类型
# print(pageSource) # 打印pageSource
# driver.close() # 关闭浏览器