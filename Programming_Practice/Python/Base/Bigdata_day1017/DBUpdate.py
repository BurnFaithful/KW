import pymysql

searchName = input("수정할 이름 : ")
updateName = input("바뀔 이름 : ")

conn = pymysql.connect(host='localhost', user='root', password='cout49!', db='KW', charset='utf8')

curs = conn.cursor()

sql = """update member set memID = %s where memID = %s"""
count = curs.execute(sql, (updateName, searchName))
conn.commit()

print(f" {count} 개 수정 완료.")
conn.close()