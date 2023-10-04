import json

filename='temperature_anomaly.json'
with open(filename,encoding="utf-8") as data:
    temps = json.load(data)

print(temps)
print(temps["description"])
print(temps["citation"])

for year,temp in temps["data"].items():
    year , temp = int(year) , float(temp)
    print(f"{year} : {temp}")

