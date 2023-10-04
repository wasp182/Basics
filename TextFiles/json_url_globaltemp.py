import json
import urllib.request

url_json ="https://www.ncdc.noaa.gov/cag/time-series/global/globe/land_ocean/ytd/12/1880-2021/data.json"

with urllib.request.urlopen(url_json) as json_stream:
    data = json_stream.read().decode('utf-8')
    temps = json.loads(data)

print(temps)

for year,temp in temps["data"].items():
    print(f"{year} : {temp}")


