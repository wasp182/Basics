import csv
filename='OlympicMedals_2020.csv'

with open(filename,encoding='utf-8',newline='') as olympics:
    header = olympics.readline().strip('\n').split(',')
    print(header)
    csv_olympics = csv.reader(olympics)
    for items in csv_olympics:
        print(items)
    # print(csv_olympics)
