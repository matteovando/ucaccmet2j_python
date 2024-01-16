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
precipitation_that_month = 0
different_months = ("-01-","-02-","-03-","-04-","-05-","-06-","-07-","-08-","-09-","-10-","-11-","-12-")
weather_dictionary_monthly = {}

for i in range(len(weather_precipitation)):
    if weather_precipitation[i]["station"] == Seattle_code:
        total_prep_Seattle += weather_precipitation[i]["value"]
        
        for specific_month in different_months:
            if specific_month in weather_precipitation[i]["date"]:
                precipitation_that_month += weather_precipitation[i]["value"]
                weather_dictionary_monthly[specific_month] = precipitation_that_month

weather_list_monthly = list(weather_dictionary_monthly.items())

correct_weather_dictionary = {}
correct_weather_dictionary["Seattle"] = {
    "station": Seattle_code,
    "state" : "WA",
    "total_monthly_precipitation" : weather_list_monthly,
    "total_yearly_precipitation" : total_prep_Seattle
    #"relative_monthly_precipitation":  xxx,
    #"relative_yearly_precipitation": xxx, 

}
with open('precipitation_results.json', 'w', encoding='utf-8') as file:
    json.dump(correct_weather_dictionary, file, indent=4)