import urllib.request
from bs4 import BeautifulSoup
import os,re
import urllib.error
from selenium import webdriver

def rename(url):
    driver = webdriver.PhantomJS(executable_path='D:\\software\\an\\python3.5.2\\Lib\\phantomjs\\bin\\phantomjs')
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'xml')
    title = soup.find("title").get_text()
    print(title)
    title0 = title[:-4]
    print(title0)
    page = soup.find("div", {"class": "column"}).find('span').get_text()
    pattern = re.compile('\d*')
    page = pattern.findall(page)
    page = int(page[0])
    print(page)
    try:
        os.rename("D:\\temp\\pic\\jiumei\\" + title, "D:\\temp\\pic\\jiumei\\" + title0 + page)
    except:
        return

if __name__ == '__main__':
    url = 'http://www.99mm.me/xinggan/'
    print('第1页')
    html = urllib.request.urlopen(url).read()
    urls = BeautifulSoup(html, 'lxml').findAll('a', href=re.compile("/xinggan/\d*?\.html"))
    quchong = []
    for url in urls:
        url = url['href']
        url = 'http://www.99mm.me' + str(url)
        quchong.append(url)
    quchong = list(set(quchong))
    print(quchong.pop())
    rename(quchong.pop())


