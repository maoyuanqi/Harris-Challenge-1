# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import json
# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open('divvy_stations.txt').read())


# PROBLEM 1
# find average number of empty docks (num_docks_available) and 
# available bikes (num_bikes_available) at all stations in the system

#first, find # of stations in the system
station_ids = set()
for record in divvy_stations:
    station_ids.add(record['station_id'])
print("total number of station is {}".format(len(station_ids)))
#second, find sum of all num_docks/bikes available, starting with docks
dock_sums = 0
for record in divvy_stations:
    dock_sums += record['num_docks_available']
print("The average number of docks available is {}".format(dock_sums/len(station_ids)))
#then bikes
bike_sums = 0
for record in divvy_stations:
    bike_sums += record['num_bikes_available']
print("The average number of bikes available is {}".format(bike_sums/len(station_ids)))



# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)

#total bikes is available + disabled.
bike_total = 0
for record in divvy_stations:
    bike_total += (record['num_bikes_available'] +record['num_bikes_disabled'])
print("ratio of bikes that are currently rented to total bikes in the system is {}".format(bike_sums/bike_total))

# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%

for record in divvy_stations:
    try:
        record.setdefault("percent_bikes_remaining",str(round(record['num_bikes_available']*100 /(record['num_bikes_available'] +record['num_bikes_disabled']),2))+"%")
    except:
        record.setdefault("percent_bikes_remaining","0%")

print(divvy_stations)

