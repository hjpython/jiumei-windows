import urllib.request
from bs4 import BeautifulSoup
import os
import shutil
import urllib.error
import pymysql
import re
from selenium import webdriver

def sql(url):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mypydb', charset='utf8')
    cur = conn.cursor()
    sql = ("insert into jiumei(url)" "values(%s)")
    cur.execute(sql, url)
    conn.commit()
    cur.close()
    conn.close()

def sqll(url):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mypydb', charset='utf8')
    cur = conn.cursor()
    sql = ("insert into jiumeim(url)" "values(%s)")
    cur.execute(sql, url)
    conn.commit()
    cur.close()
    conn.close()

def xiazai_jiumei(url):
    driver = webdriver.PhantomJS(executable_path='D:\\software\\an\\python3.5.2\\Lib\\phantomjs\\bin\\phantomjs')
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'xml')
    title = soup.find("title").get_text()
    title = title[:-4]
    page = soup.find("div",{"class": "column"}).find('span').get_text()
    pattern = re.compile('\d*')
    page = pattern.findall(page)
    page = int(page[0])
    try:
        os.makedirs("D:\\temp\\pic\\jiumei\\" + title + page)
    except:
        return
    pages = page + 1
    for i in range(1,pages):
        try:
            urll = url + '?url='+str(i)
            driver = webdriver.PhantomJS(executable_path='D:\\software\\an\\python3.5.2\\Lib\\phantomjs\\bin\\phantomjs')
            driver.get(urll)
            soup = BeautifulSoup(driver.page_source, 'xml')
            picurl = soup.find("div",{"id":"picbox"}).find('img')['src']
            img = urllib.request.urlopen(picurl).read()
            f = open("D:\\temp\\pic\\jiumei\\" + title + page + "\\" + str(i) + ".jpg","wb")
            f.write(img)
            f.close()
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
                sql(url)
                print('未下载网址已存入数据库')
                continue
            elif hasattr(e,"reason"):
                print(e.reason)
                sql(url)
                print('未下载网址已存入数据库')
                continue

def xiazai_jiumei_sql(url):
    driver = webdriver.PhantomJS(executable_path='D:\\software\\an\\python3.5.2\\Lib\\phantomjs\\bin\\phantomjs')
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'xml')
    title = soup.find("title").get_text()
    title = title[:-4]
    page = soup.find("div", {"class": "column"}).find('span').get_text()
    pattern = re.compile('\d*')
    page = pattern.findall(page)
    page = int(page[0])
    try:
        os.makedirs("D:\\temp\\pic\\jiumei\\" + title + page)
    except:
        shutil.rmtree("D:\\temp\\pic\\jiumei\\" + title + page)
        os.makedirs("D:\\temp\\pic\\jiumei\\" + title + page)

    pages = page + 1
    for i in range(1,pages):
        try:
            urll = url + '?url=' + str(i)
            driver = webdriver.PhantomJS(executable_path='D:\\software\\an\\python3.5.2\\Lib\\phantomjs\\bin\\phantomjs')
            driver.get(urll)
            soup = BeautifulSoup(driver.page_source, 'xml')
            picurl = soup.find("div", {"id": "picbox"}).find('img')['src']
            img = urllib.request.urlopen(picurl).read()
            f = open("D:\\temp\\pic\\jiumei\\" + title + page + "\\" + str(i) + ".jpg", "wb")
            f.write(img)
            f.close()
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
                sqll(url)
                print('未下载网址已存入数据库')
            elif hasattr(e,"reason"):
                print(e.reason)
                sqll(url)
                print('未下载网址已存入数据库')
        finally:
            continue