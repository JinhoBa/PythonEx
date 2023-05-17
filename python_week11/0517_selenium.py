#뉴스 가져오기
# pip install selenium
# pip install webdriver_manager
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

# 1. 뉴스가져오기
'''
driver.get("https://www.naver.com/")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[3]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(10)'''
'''
driver.get("https://1xbet.whoscored.com/")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[3]/ul/li[1]/a").click()
time.sleep(5)

pl_table = driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div[1]/div[9]/div[2]/div[2]").text
print(pl_table)
driver.find_element(By.XPATH,"/html/body/div[4]/div[5]/div[2]/div[4]/div/dl[2]/dd[3]/a").click()
time.sleep(5)
print(pl_table)'''

#부동산 가격 (오류남)
'''
driver.get("https://m.land.naver.com/")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/header/div/div[2]/a[1]/i").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").send_keys("마곡엠벨리7단지")
time.sleep(5)
rentprice = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/dl/dd[1]").text
print(rentprice)
'''

# 주식 가져오기
driver.get("https://finance.naver.com/")
lst = []
lst2 = []
for i in range(10):
    sub = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/th/a").text
    per = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[3]").text
    lst.append(sub)
    lst2.append(per)
for i in range(10):
    print(lst[i], lst2[i])

'''
driver.get("https://finance.naver.com/")
time.sleep(1)
sub1 = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/th/a").text
time.sleep(1)
sub2 = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[2]/th/a").text
time.sleep(1)
sub3 = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[3]/th/a").text
time.sleep(1)
print(sub1,sub2,sub3)
'''