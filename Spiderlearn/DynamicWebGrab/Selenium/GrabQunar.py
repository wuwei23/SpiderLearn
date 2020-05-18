from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import codecs
import datetime

class QunarSpider(object):

    def get_hotel(self, driver, to_city, fromdate, todate):

        #进入界面
        ele_toCity = driver.find_element_by_class_name('inputText')
        ele_fromdate = driver.find_element_by_xpath('//input[@tabindex="2"]')
        ele_todate = driver.find_element_by_xpath('//input[@tabindex="3"]')
        #ele_search = driver.find_element_by_class_name('main')
        ele_search = driver.find_element_by_xpath('//a[@tabindex="5"]')

        ele_toCity.clear()
        ele_toCity.send_keys(to_city)
        time.sleep(2)
        #ele_toCity.click()
        ele_fromdate.clear()
        ele_fromdate.send_keys(fromdate)
        ele_todate.clear()
        ele_todate.send_keys(todate)
        time.sleep(2)
        ele_search.click()
        time.sleep(3)

        ele_close = driver.find_element_by_class_name('alert-container-closer')
        ele_close.click()

        page_num = 0
        while True:
            #检查当前页面title是否包含to_city
            try:
                WebDriverWait(driver, 10).until(
                    EC.title_contains(str(to_city))
                )
            except Exception as e:
                print(e)
                break
            print("###" * 10)
            #跳到页面末尾让加载完成
            js = "window.scrollTo(0, document.body.scrollHeight);"
            driver.execute_script(js)
            time.sleep(5)
            print("###"*10)
            #清洗数据
            htm_const = driver.page_source
            #print(htm_const)

            soup = BeautifulSoup(htm_const, 'html.parser', from_encoding='utf-8')
            #print(soup.prettify())
            infos = soup.find_all(class_ = "hotel-name")
            print(infos)
            f = codecs.open(str(to_city)+str(fromdate) + u'.txt', 'a', 'utf-8')
            f.write(str(page_num) + '--' * 50 + '\r\n')
            for info in infos:
                content = info.get_text().replace(" ","").replace("\t","").strip()
                for line in [ln for ln in content.splitlines() if ln.strip()]:
                    f.write(line)
                    f.write('\r\n')
            try:
                next_page = WebDriverWait(driver, 10).until(
                    EC.visibility_of(driver.find_element_by_class_name("next"))
                )
                time.sleep(3)
                next_page.click()
                page_num+=1
                time.sleep(8)
            except Exception as e:
                print(e)
                break
            f.close()

    def crawl(self,root_url, to_city):
        today = datetime.date.today().strftime('%Y-%m-%d')
        tomorrow = datetime.date.today()+datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime('%Y-%m-%d')
        driver = webdriver.Chrome()
        driver.set_page_load_timeout(50)
        driver.get(root_url)
        driver.maximize_window()#浏览器最大化显示
        driver.implicitly_wait(10)#控制间隔时间 等待浏览器反应
        self.get_hotel(driver, to_city, today, tomorrow)


if __name__ == '__main__':
    spider = QunarSpider()
    spider.crawl('https://hotel.qunar.com/', u'上海')