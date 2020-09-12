import pymysql

deleteName = input("삭제할 이름 : ")

conn = pymysql.connect(host='localhost', user='root', password='cout49!', db='KW', charset='utf8')

curs = conn.cursor()

sql = """delete from member where memID = %s"""
count = curs.execute(sql, deleteName)
conn.commit()

print(f"{count}개 삭제 완료.")