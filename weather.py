import json
import csv

weather_info = csv.DictReader(open("stations.csv"))
weather_list = []
for weather in weather_info:
    weather_list.append(weather['Station'])
Seattle_code = (weather_list[2])
#print(Seattle_code)

weather_code = open('precipitation.json')
weather_precipitation = json.load(weather_code)

total_prep_Seattle = 0
precipitation_that_month = 0
different_months = ("-01-","-02-","-03-","-04-","-05-","-06-","-07-","-08-","-09-","-10-","-11-","-12-")
weather_dictionary = {}

for i in range(len(weather_precipitation)):
    if weather_precipitation[i]["station"] == Seattle_code:
        total_prep_Seattle += weather_precipitation[i]["value"]
        
        for specific_month in different_months:
            if specific_month in weather_precipitation[i]["date"]:
                precipitation_that_month += weather_precipitation[i]["value"]
                weather_dictionary[specific_month] = precipitation_that_month
            
print(weather_dictionary)


print(total_prep_Seattle)
    


