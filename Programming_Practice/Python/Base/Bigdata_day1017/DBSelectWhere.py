import pymysql

ser_name = input("검색할 회원 ID : ")

conn = pymysql.connect(host='localhost', user='root', password='cout49!', db='KW', charset='utf8')

curs = conn.cursor()

sql = "select * from member where memID = %s"

curs.execute(sql, ser_name)

rows = curs.fetchall()
for row in rows:
    # print(row)
    print(row[0], row[1])

conn.close()