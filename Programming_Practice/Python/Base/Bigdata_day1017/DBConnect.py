import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='cout49!',
                       db='KW',
                       charset='utf8')

curs = conn.cursor() # DB 테이블 및 결과셋에 커서 연결

sql = "select * from member" # 쿼리문
curs.execute(sql)

rows = curs.fetchall()
print(rows)

conn.close()