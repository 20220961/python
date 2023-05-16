## import 구문 쓸때 213교실 F1 >> 인터프리터 >> base

from bs4 import BeautifulSoup as B
import requests as r

headers={
    "User-Agent":"Dong Yang Mirea Univ"
}
'''
news1 = r.get("https://sports.news.naver.com/news?oid=076&aid=0004007685")
## print(news1) ## Request 200이 뜨면 성공
soup = B(news1.content,"html.parser") ## html 소스 받아오기
### print(soup)

news2 = soup.select_one("#newsEndContents").get_text().strip()
## print(news2)

# pip3 install selenium
# pip install webdriver_manager
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# chrome_options = Opthions()
# chrome_options.add_experimental_option("detach",True)
# chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
'''
driver.get("https://www.naver.com/")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/section/header/div[1]/div/div/div[1]/div/span[2]/a/span").click()
time.sleep(3)
a = driver.find_element(By.XPATH,"/html/body/div[4]/header/nav[1]/ul/li[13]/a").text
print(a)

driver.get("https://m.land.naver.com/search")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").send_keys("서울시 구로구 벽산베스트블루밍")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]").click()
time.sleep(1)
meme = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div").text
time.sleep(1)
print(meme)

'''

driver.get("https://finance.naver.com/")
time.sleep(1)
lst = []
for i in range(10):
    top = driver.find_element(By.XPATH,f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/th").text
    lst.append(top)

print(lst)

driver.get("https://sports.news.naver.com/kbaseball/index")
time.sleep(1)
lstt = []
for i in range(10):
    topp = driver.find_element(By.XPATH,f"/html/body/div[4]/div[1]/div[3]/div/div[3]/div[4]/div[3]/div/div[2]/table/tbody/tr[{i+1}]/td[1]").text
    lstt.append(topp)

print(lstt)