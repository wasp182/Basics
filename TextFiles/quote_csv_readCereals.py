import csv

filename = "cereal_grains.csv"

with open(filename, encoding='utf-8' , newline="") as data:
    csv_data = csv.reader(data,quoting= csv.QUOTE_NONNUMERIC)
    # assumes all non numeric data as quoted
    for lines in csv_data:
        print(lines)