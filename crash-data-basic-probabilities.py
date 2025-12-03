import pandas as pd
import numpy as np
import matplotlib.pyplot as plotter
import seaborn as sb
# import glob
# import os


# --- Read in crash data csv files ---
# crash_data_2021= pd.read_csv('assets/2021-Crash-Data-Normalized.csv')
# crash_data_2022 = pd.read_csv('assets/2022-Crash-Data-Normalized.csv')
# crash_data_2023= pd.read_csv('assets/2023-Crash-Data-Normalized.csv')
# crash_data_2024 = pd.read_csv('assets/2024-Crash-Data-Normalized.csv')

crash_data = pd.read_csv('assets/all_crash_data.csv')
crash_data_frame = pd.DataFrame(crash_data) 

# crash_data_files = glob.glob("assets/*.csv")

# crash_data_frames = []
# for file in crash_data_files:
#     crash_data_frames.append(pd.read_csv(file))
    
# crash_data_frame = pd.concat(crash_data_frames, ignore_index=True)

# num_crashes = len(crash_data_frame)
# print(num_crashes)

# --- Count of crashes in 2024 ---
num_crashes_2024 = crash_data["CUID"].count()

# --- Wild animal related crashes ---
num_wild_animal = crash_data["Wild Animal"].count()
wild_animal_prob_percent = (num_wild_animal / num_crashes_2024 ) * 100

# print(f'Num accidents involving a wild animal: {num_wild_animal}')
print(f'Probability of accident involving a wild animal: {wild_animal_prob_percent} \n')

# --- School zone related crashes ---
num_school_zone = crash_data["School Zone"].sum()
school_zone_prob_percent = (num_school_zone / num_crashes_2024 ) * 100

# print(f'Num accidents occuring in a school zone: {num_school_zone}')
print(f'Probability of accident occuring in a school zone: {school_zone_prob_percent} \n')

# --- Construction zone related crashes --- 
num_construction_zone = crash_data["Construction Zone"].sum()
construction_zone_prob_percent = (num_construction_zone / num_crashes_2024 ) * 100

# print(f'Num accidents occuring in a construction zone: {num_construction_zone}')
print(f'Probability of accident occuring in a construction zone: {construction_zone_prob_percent} \n')


# Plot Zone and Animal Related Probabilities

categories = ["Wild Animals", "School Zone", "Construction Zone"]
probs = [wild_animal_prob_percent, school_zone_prob_percent, construction_zone_prob_percent]

plotter.bar(categories, probs)
plotter.ylabel("Probability (%)")
plotter.title("Zone and Animal Related Crash Probabilities")
plotter.show()

# --- Weather related crashes ---
# Conditions: Blowing Snow, Clear, Cloudy, Dust, Fog, Freezing Rain or Freezing 
    # Drizzle, Rain, Sleet or Hail, Snow, Unknown, Wind
    
# create weather conditions count DataFrame    
weather_counts = crash_data_frame["Weather Condition"].value_counts()

# get counts accidents by weather conditions
weather_conditions = [
    "Blowing Snow", 
    "Clear", 
    "Cloudy", 
    "Dust", 
    "Fog", 
    "Freezing Rain", 
    "Rain", 
    "Sleet or Hail", 
    "Snow", 
    "Unknown", 
    "Wind"]

weather_condition_counts = [] # empty list to store counts

for condition in weather_conditions:
    # print(f'Condition: {condition}')
    weather_condition_counts.append(weather_counts.get(condition))

# calculate weather condition probabilities
weather_condition_probabilities = [] # empty list to store probability 
                                     # percentage %

for condition_count in weather_condition_counts:
    # print(condition_count)
    prob = (condition_count / num_crashes_2024) * 100
    weather_condition_probabilities.append(prob)


# Print probability of accident occuring under various weather conditiosn
for i in range(0, len(weather_conditions)):
    condition = weather_conditions[i]
    condition_probability = weather_condition_probabilities[i]
    if (i == len(weather_conditions) - 1):
        print(f'Probability of accident occurring under {condition} conditions: {condition_probability} \n')
    else:
        print(f'Probability of accident occurring under {condition} conditions: {condition_probability}')
        

# plot weather conditions probs
plotter.bar(weather_conditions, weather_condition_probabilities)
plotter.ylabel("Probability (%)")
plotter.title("Weather Condition Crash Probabilities")
plotter.show()

# --- Road Location related crashes ---

# get counts accidents by location

locations = [
    "City Street",
    "State Highway",
    "Interstate Highway",
    "County Road",
    "Frontage Road"
]

location_crash_counts = crash_data_frame["System Code"].value_counts()


location_counts = [] # empty list to store counts

# get crash counts by location
for location in locations: 
    location_counts.append(location_crash_counts.get(location))

# calculate location probabilities   
location_probs = [] # empty list to store probabilities of crash at location as 
                    # percent %

for count in location_counts:
    prob = (count / num_crashes_2024) * 100
    location_probs.append(prob)
    
# Print probability of accident occuring at each location    
for i in range(0, len(locations)):
    location = locations[i]
    location_prob = location_probs[i]
    
    if (i == len(locations) - 1):
        print(f'Probability of accident occurring on a {location}: {location_prob} \n')
    else:
        print(f'Probability of accident occurring on a {location}: {location_prob}')
        
# plot location probs
plotter.bar(locations, location_probs)
plotter.ylabel("Probability (%)")
plotter.title("Crash Location Probabilities")
plotter.show()

# --- Road Condition related crashes ---

# get counts accidents by road condition

road_conditions_lst = [
    "Dry",
    "Dry /Treated",
    "Foreign Material",
    "Icy",
    "Icy /Treated",
    "Muddy",
    "Roto-Milled",
    "Sand/Gravel",
    "Slushy",
    "Slushy /Treated",
    "Snowy",
    "Snowy /Treated",
    "Unknown",
    "Wet",
    "Wet /Treated"
]

road_condition_counts = crash_data_frame["Road Condition"].value_counts()


road_condition_counts_lst = [] # empty list to store counts

# get crash counts by road condition
for condition in road_conditions_lst: 
    road_condition_counts_lst.append(road_condition_counts.get(condition))

# calculate condition probabilities   
road_condition_probs_lst = [] # empty list to store probabilities of crash under
                              # condition as percent %

for count in road_condition_counts_lst:
    prob = (count / num_crashes_2024) * 100
    road_condition_probs_lst.append(prob)
    
# Print probability of accident under at each condition    
for i in range(0, len(road_conditions_lst)):
    road_condition = road_conditions_lst[i]
    road_condition_prob = road_condition_probs_lst[i]
    
    if (i == len(road_conditions_lst) - 1):
        print(f'Probability of accident occurring on a {road_condition}: {road_condition_prob} \n')
    else:
        print(f'Probability of accident occurring on a {road_condition}: {road_condition_prob}')
        
# plot conditon probs
plotter.bar(road_conditions_lst, road_condition_probs_lst)
plotter.ylabel("Probability (%)")
plotter.title("Road Condition Crash Probabilities")
plotter.show()


# --- Driver Action related crashes ---

# get counts accidents by driver action (condition)

driver_action_counts = crash_data_frame["Driver Action"].value_counts()
# print("Driver Action Counts: ", driver_action_counts)

driver_action_lst = []
driver_action_probs_lst = []

for action, count in driver_action_counts.items():
    driver_action_lst.append(action)
    prob = (count / num_crashes_2024) * 100
    driver_action_probs_lst.append(prob)
    print(f'Probability of accident occurring due to {action}: {prob}')

# plot action probs
plotter.bar(driver_action_lst, driver_action_probs_lst)
plotter.ylabel("Probability (%)")
plotter.title("Driver Action Crash Probabilities")
plotter.show()