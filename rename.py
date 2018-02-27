import urllib.request
from bs4 import BeautifulSoup
import os,re
import urllib.error
from selenium import webdriver
from multiprocessing import Pool

def rename(url):
    driver = webdriver.PhantomJS(executable_path='D:\\software\\an\\python3.5.2\\Lib\\phantomjs\\bin\\phantomjs')
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'xml')
    title = soup.find("title").get_text()
    title0 = title[:-4]
    page = soup.find("div", {"class": "column"}).find('span').get_text()
    pattern = re.compile('\d*')
    page = pattern.findall(page)
    page = page[0]
    try:
        os.rename("D:\\temp\\pic\\jiumei\\" + title, "D:\\temp\\pic\\jiumei\\" + title0 + page)
    except:
        return

if __name__ == '__main__':
    p = Pool(10)
    #更改第1页的名字
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
    for url in quchong:
        print(url)
        p.apply_async(rename, args=(url,))

    # 更改第2到95页的名字
    for i in range(2,96):
        print("第"+str(i)+"页")
        url = 'http://www.99mm.me/xinggan/mm_2_'+str(i)+'.html'
        html = urllib.request.urlopen(url).read()
        urls = BeautifulSoup(html, 'lxml').findAll('a', href=re.compile("/xinggan/\d*?\.html"))
        quchong = []
        for url in urls:
            url = url['href']
            url = 'http://www.99mm.me' + str(url)
            quchong.append(url)
        quchong = list(set(quchong))
        for url in quchong:
            print(url)
            p.apply_async(rename, args=(url,))
    p.close()
    p.join()
    print('恭喜您，已全部更改完毕')