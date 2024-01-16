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

# count variables and useful strings for further JSON file

total_prep_Seattle = 0
precipitation_that_month = 0
different_months = ("-01-","-02-","-03-","-04-","-05-","-06-","-07-","-08-","-09-","-10-","-11-","-12-")
names_states = ("Cincinnati", "Seattle", "Maui", "San Diego")
initials_states = ("OH", "WA", "HI","CA") 

#CREATE AN EMPTY DICTIONARY 

weather_dictionary_monthly = {}

# a loop that analyzes the codes of every entry and creates a key of the state if needed. Furthermore, inside 
# each of the state keys it creates an initial key with the total precipitation and then 12 keys for the precipitations
# of each month of each state

for i in range(len(weather_precipitation)):
    for code in state_codes:
        if weather_precipitation[i]["station"] == code:
            #create state keys
            if code not in weather_dictionary_monthly:
                weather_dictionary_monthly[code] = {}
            #total precipitations per state
            total_prep_state = weather_dictionary_monthly[code].get(f'total_prepecipitation({code})', 0)
            total_prep_state += weather_precipitation[i]["value"]           
            weather_dictionary_monthly[code][f'total_prepecipitation({code})'] = total_prep_state
            #monthly precipitation per state
            for specific_month in different_months:
                if specific_month in weather_precipitation[i]["date"]:
                    if specific_month not in weather_dictionary_monthly[code]:
                        weather_dictionary_monthly[code][specific_month] = 0

                    precipitation_that_month = weather_dictionary_monthly[code][specific_month]
                    precipitation_that_month += weather_precipitation[i]["value"]
                    weather_dictionary_monthly[code][specific_month] = precipitation_that_month

# RELATIVE PRECIPITATION #

#weather_list_monthly = list(weather_dictionary_monthly.values()) # useful to convert dictionary in list.
# Would've made use in next step or maybe just a .append with every key       

#I didnt have time to do this for the general case, however I would do it through a for loop that has the keys
# of the different states and would access the inner dictionaries. At this level I could either make another for 
# loop that uses all the keys of the months and would transfer them as lists or simply just start an indexed
# loop not from 0, which would select the total precipitation, but from 1 to 12.            

relative_prec = []

for each_month in weather_list_monthly:
    relative_prec.append(each_month/total_prep_state[Seattle_code]* 100)
        
#CREATE JSON FILE#
    
#attempt to create a big for loop with all the different components of our JSON file. However I didnt have time to
#do the relative precipitations. 

correct_weather_dictionary = {}

# would have needed a few more for loops to go through all the mpnthly, yearly and relative precipitations lists or values #

for state_name in names_states:
    for code in state_codes: 
        for ini_state in initials_states:
            
            correct_weather_dictionary[f"{state_name}"] = {
                "station": code,
                "state" : f"{ini_state}",
                "total_monthly_precipitation" : weather_list_monthly,
                "total_yearly_precipitation" : total_prep_state[Seattle_code],
                "relative_monthly_precipitation": relative_prec
                #"relative_yearly_precipitation": xxx, 
}

   
with open('precipitation_results.json', 'w', encoding='utf-8') as file:
    json.dump(correct_weather_dictionary, file, indent=4)