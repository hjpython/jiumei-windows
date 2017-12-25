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
def xiazai_jiumei_sql(url):
    driver = webdriver.PhantomJS()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'xml')
    title = soup.find("title").get_text()
    page = soup.find("div", {"class": "column"}).find('span').get_text()
    pattern = re.compile('\d*')
    page = pattern.findall(page)
    try:
        os.makedirs(r"/home/hj/python/pic/jiumei/"+str(title))
    except:         
        shutil.rmtree(r"/home/hj/python/pic/jiumei/"+str(title))
        os.makedirs(r"/home/hj/python/pic/jiumei/"+str(title))
    after = int(page[0])+1
    for i in range(1,after):
        try:
            urll = url + '?url=' + str(i)
            driver = webdriver.PhantomJS()
            driver.get(urll)
            soup = BeautifulSoup(driver.page_source, 'xml')
            picurl = soup.find("div", {"id": "picbox"}).find('img')['src']
            img = urllib.request.urlopen(picurl).read()
            f = open("/home/hj/python/pic/jiumei/" + title + "/" + str(i) + ".jpg", "wb")
            f.write(img)
            f.close()
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
                conn = pymysql.connect(host='192.168.0.131',user='root',passwd='123456',db='mypydb',charset='utf8')
                cur = conn.cursor()
                sql = ("insert into jiumeim(url)" "values(%s)")
                cur.execute(sql,url)
                conn.commit()
                cur.close()
                conn.close()
                print('未下载网址已存入数据库')
                continue
            if hasattr(e,"reason"):
                print(e.reason)
                conn = pymysql.connect(host='192.168.0.131',user='root',passwd='123456',db='mypydb',charset='utf8')
                cur = conn.cursor()
                sql = ("insert into jiumeim(url)" "values(%s)")
                cur.execute(sql,url)
                conn.commit()
                cur.close()
                conn.close()
                print('未下载网址已存入数据库')
                continue
if __name__ == '__main__':
    urls = []
    conn = pymysql.connect(host='192.168.0.131',user='root',passwd='123456',db='mypydb',charset='utf8')
    cur = conn.cursor()
    cur.execute("select url from jiumei")
    results = cur.fetchall()
    cur.close()
    conn.close()
    result = list(results)
    for r in result:
        urls.append("%s"%r)
    urls = list(set(urls))
    while urls:
        url = urls.pop()
        print("重新下载:%s"%url)
        xiazai_jiumei_sql(url)
        try:
            conn = pymysql.connect(host='192.168.0.131',user='root',passwd='123456',db='mypydb',charset='utf8')
            cur = conn.cursor()
            cur.execute("select url from jiumeim")
            results = cur.fetchall()
            cur.execute("truncate jiumeim")
            cur.close()
            conn.close()
            result = list(results)
            for r in result:
                urls.append("%s"%r)
            urls = list(set(urls))
        except:
            pass