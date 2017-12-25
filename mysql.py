import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
cur = conn.cursor()
cur.execute("select url from jiumeim")
cur.execute("truncate jiumeim")
cur.close()
conn.close()