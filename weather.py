import json
import csv

#### LOAD CSV AND JSON ##############
weather_info = csv.DictReader(open("stations.csv"))
weather_list = []
for weather in weather_info:
    weather_list.append(weather['Station'])

weather_code = open('precipitation.json')
weather_precipitation = json.load(weather_code)

##################################
#### CODES FOR EVERY LOCATION ####
Cincinnati_code = (weather_list[0])
Seattle_code = (weather_list[1])
Maui_code = (weather_list[2])
SanDiego_code = (weather_list[3])

state_codes = (Cincinnati_code, Seattle_code, Maui_code, SanDiego_code)
###############################

total_prep_Seattle = 0
precipitation_that_month = 0
different_months = ("-01-","-02-","-03-","-04-","-05-","-06-","-07-","-08-","-09-","-10-","-11-","-12-")
weather_dictionary_monthly = {}

#total_prep_Seattle is total precipitation that year and precipitation_that_month is precipitation for every month#

for i in range(len(weather_precipitation)):
    if weather_precipitation[i]["station"] == Seattle_code:
        total_prep_Seattle += weather_precipitation[i]["value"]
        
        for specific_month in different_months:
            if specific_month in weather_precipitation[i]["date"]:
                precipitation_that_month += weather_precipitation[i]["value"]
                weather_dictionary_monthly[specific_month] = precipitation_that_month

#TRANSFORM DICTIONARY TO LIST#
weather_list_monthly = list(weather_dictionary_monthly.values())


# TOTAL YEARLY PER LOCATION (not just Seattle) #
total_prep_state = {}

for i in range(len(weather_precipitation)):
    for singstate in state_codes:
        if weather_precipitation[i]["station"] == singstate:  

            if singstate not in total_prep_state:
                total_prep_state[singstate] = 0            
            
            total_prep_state[singstate] += weather_precipitation[i]["value"]

# RELATIVE PRECIPITATION #
relative_prec = []

print(weather_list_monthly)
#print(total_prep_state[Seattle_code])

for each_month in weather_list_monthly:
    relative_prec.append(each_month/total_prep_state[Seattle_code]* 100)
        






#CREATE JSON FILE#
correct_weather_dictionary = {}
correct_weather_dictionary["Seattle"] = {
    "station": Seattle_code,
    "state" : "WA",
    "total_monthly_precipitation" : weather_list_monthly,
    "total_yearly_precipitation" : total_prep_state[Seattle_code],
    "relative_monthly_precipitation": relative_prec
    #"relative_yearly_precipitation": xxx, 
}
correct_weather_dictionary["Cincinnati"] = {
    "station": Cincinnati_code,
    "state" : "OH",
    #"total_monthly_precipitation" : xxx,
    "total_yearly_precipitation" : total_prep_state[Cincinnati_code]
   
}






with open('precipitation_results.json', 'w', encoding='utf-8') as file:
    json.dump(correct_weather_dictionary, file, indent=4)