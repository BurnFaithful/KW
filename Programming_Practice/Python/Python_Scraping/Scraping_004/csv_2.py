import csv, codecs

filename = "test.csv"
fp = codecs.open(filename, "r", "euc_kr")

reader = csv.reader(fp, delimiter=',', quotechar='"')
for cells in reader:
    print(cells[0], cells[1], cells[2])