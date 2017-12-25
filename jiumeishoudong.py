#!/usr/bin/env python
# coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
import os
import shutil
import urllib.error
import pymysql
import re
from selenium import webdriver
def xiazai_jiumei(url):
    driver = webdriver.PhantomJS(executable_path='D:\\software\\an\\python3.5.2\\Lib\\phantomjs\\bin\\phantomjs')
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'xml')
    title = soup.find("title").get_text()
    page = soup.find("div",{"class":"column"}).find('span').get_text()
    pattern = re.compile('\d*')
    page = pattern.findall(page)
    try:
        os.makedirs("D:\\temp\\pic\\jiumei\\"+str(title))
    except:
        shutil.rmtree("D:\\temp\\pic\\jiumei\\"+str(title))
        os.makedirs("D:\\temp\\pic\\jiumei\\"+str(title))
    after = int(page[0])+1
    for i in range(1,after):
        try:
            urll = url + '?url='+str(i)
            driver = webdriver.PhantomJS(executable_path='D:\\software\\an\\python3.5.2\\Lib\\phantomjs\\bin\\phantomjs')
            driver.get(urll)
            soup = BeautifulSoup(driver.page_source, 'xml')
            picurl = soup.find("div",{"id":"picbox"}).find('img')['src']
            img = urllib.request.urlopen(picurl).read()
            f = open("D:\\temp\\pic\\jiumei\\"+title+"\\"+str(i)+".jpg","wb")
            f.write(img)                 
            f.close()
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
                continue
            if hasattr(e,"reason"):
                print(e.reason)
                continue
if __name__ == '__main__':
    while True:
        url = input("请输入网址：")
        xiazai_jiumei(url)
