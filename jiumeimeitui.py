from factor import *

if __name__ == '__main__':
    url = 'http://www.99mm.me/meitui/'
    print('第' + str(1) + '页')
    html = urllib.request.urlopen(url).read()
    urls = BeautifulSoup(html,'lxml').findAll('a',href=re.compile("/meitui/\d*?\.html"))
    quchong = []
    for url in urls:
        url = url['href']
        url = 'http://www.99mm.me'+str(url)
        quchong.append(url)
    quchong = list(set(quchong))
    for url in quchong:
        print(url)
        xiazai_jiumei(url)
    for i in range(24,25):
        print("第"+str(i)+"页")
        url = 'http://www.99mm.me/meitui/mm_1_'+str(i)+'.html'
        html = urllib.request.urlopen(url).read()
        urls = BeautifulSoup(html, 'lxml').findAll('a', href=re.compile("/meitui/\d*?\.html"))
        quchong = []
        for url in urls:
            url = url['href']
            url = 'http://www.99mm.me' + str(url)
            quchong.append(url)
        quchong = list(set(quchong))
        for url in quchong:
            print(url)
            xiazai_jiumei(url)
    urls = []
    conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
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
            conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
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
