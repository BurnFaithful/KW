import pymysql

insertName = input("추가할 이름 : ")

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='cout49!',
                       db='KW',
                       charset='utf8')

curs = conn.cursor() # DB 테이블 및 결과셋에 커서 연결

insertData = (("Moon"), ("Lee"), ("Oh"))

sql = """insert into member(memID) values(%s)"""
# curs.execute(sql, insertName)
curs.executemany(sql, insertData)
conn.commit()

conn.close()