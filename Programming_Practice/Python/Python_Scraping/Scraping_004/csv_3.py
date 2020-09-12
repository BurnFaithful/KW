import openpyxl

filename = "test_02.xlsx"
book = openpyxl.load_workbook(filename)

# 2018년 인구 최소 5개 자치 행정구역
# sheet = book.worksheets[0]
#
# data = list()
#
# for row in sheet.rows:
#     data.append([row[0].value, row[10].value])
#
# del (data[0], data[1], data[2])
#
# data = sorted(data, key=lambda x:x[1])
#
# for i, a in enumerate(data):
#     if i >= 5:
#         break
#     print(i + 1, a[0], int(a[1]))


# 서울 인구를 제외한 합계 인구
sheet = book.active

for i in range(9):
    total = int(sheet[str(chr(i + 66)) + "3"].value)
    seoul = int(sheet[str(chr(i + 66)) + "4"].value)
    output = total - seoul
    print("서울 제외 인구 =", output)

    sheet[str(chr(i + 66)) + "21"] = output
    cell = sheet[str(chr(i + 66)) + "21"]
    cell.font = openpyxl.styles.Font(size=14, color="FF0000")
    cell.number_format = cell.number_format

filename = "population.xlsx"
book.save(filename)
print("save ok")