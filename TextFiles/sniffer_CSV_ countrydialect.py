import csv
filename='country_info.txt'
with open(filename, encoding='utf-8',newline="") as data:
    sample_data=""
    for i in range(3):
        sample_data += data.readline()
    dialects_data = csv.Sniffer().sniff(sample_data)

    #inputs/reads enture data stream  into sample and finds delimiters in
    #dialect variable and moves to end of file with nothing left to read
    # add seek method to go back to beginning of stream to read it again in csv
    ##  code using read() method is inefficient  also uses entire data stream as sample ,
    ## size parameter avaialbel in read method
    ##  but that requries guess on how many chacters required to
    ## create sufficiently long sample , instead we use readline() method
    data.seek(0)
    csv_data = csv.reader(data,dialect=dialects_data)
    for lines in csv_data:
        print(lines)

print("*"*80)

attributes =[
        "delimiter",
        "doublequote",
        "escapechar",
        "lineterminator",
        "quotechar",
        "quoting",
        "skipinitialspace"
            ]
for attribute in attributes:
    print(f"{attribute}: {getattr(dialects_data,attribute)}")
