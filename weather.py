import json
import csv

weather_info = csv.DictReader(open("stations.csv"))
weather_list = []
for weather in weather_info:
    weather_list.append(weather['Station'])
Seattle_code = (weather_list[2])
print(Seattle_code)

weather_code = open('precipitation.json')
weather_precipitation = json.load(weather_code)

total_prep_Seattle = 0

for i in range(len(weather_precipitation)):
    if weather_precipitation[i]["station"] == Seattle_code:
        total_prep_Seattle += weather_precipitation[i]["value"]
    
print(total_prep_Seattle)