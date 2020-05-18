from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
assert u'百度' in driver.title
elem = driver.find_element_by_name('wd') #wd输入框的name
elem.clear()
elem.send_keys(u"网络爬虫")
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert u"网络爬虫." not in driver.page_source
driver.close()