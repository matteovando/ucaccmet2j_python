import json
import csv

weather_info = csv.DictReader(open("stations.csv"))

weather_list = []

for weather in weather_info:
    weather_list.append(weather['Station'])



Seattle_code = (weather_list[2])

print(Seattle_code)