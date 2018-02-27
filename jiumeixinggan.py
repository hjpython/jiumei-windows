#!/usr/bin/env python
# coding=utf-8
from factor import *
from multiprocessing import Pool

if __name__ == '__main__':
    p = Pool(50)
    #下载第1页图片
    url = 'http://www.99mm.me/xinggan/'
    print('第1页')
    html = urllib.request.urlopen(url).read()
    urls = BeautifulSoup(html,'lxml').findAll('a',href=re.compile("/xinggan/\d*?\.html"))
    quchong = []
    for url in urls:
        url = url['href']
        url = 'http://www.99mm.me'+str(url)
        quchong.append(url)
    quchong = list(set(quchong))
    for url in quchong:
        print(url)
        p.apply_async(xiazai_jiumei, args=(url,))

    #下载第2到95页图片
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
            p.apply_async(xiazai_jiumei, args=(url,))
    p.close()
    p.join()
    print('恭喜您，已全部下载完毕')

    #下载数据库中图片
    # urls = []
    # conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
    # cur = conn.cursor()
    # cur.execute("select url from jiumei")
    # results = cur.fetchall()
    # cur.close()
    # conn.close()
    # result = list(results)
    # for r in result:
    #     urls.append("%s"%r)
    # urls = list(set(urls))
    # while urls:
    #     url = urls.pop()
    #     print("重新下载:%s"%url)
    #     xiazai_jiumei_sql(url)
    #     try:
    #         conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
    #         cur = conn.cursor()
    #         cur.execute("select url from jiumeim")
    #         results = cur.fetchall()
    #         cur.execute("truncate jiumeim")
    #         cur.close()
    #         conn.close()
    #         result = list(results)
    #         for r in result:
    #             urls.append("%s"%r)
    #         urls = list(set(urls))
    #     except:
    #         pass
