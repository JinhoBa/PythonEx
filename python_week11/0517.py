#0517
#pip bs4 import beautifulsoup4
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
headers = {
    "User-Agent":"Dongyang Jinho"
}
webpage = requests.get("https://sports.news.naver.com/news?oid=065&aid=0000246848", headers)
#print(webpage)
#print(webpage.content)

soup = BeautifulSoup(webpage.content, "html.parser")
#print(soup)

news = soup.select_one("#newsEndContents").getText().strip()
print(news)

t = soup.select_one("#header").getText().strip()
print(t)