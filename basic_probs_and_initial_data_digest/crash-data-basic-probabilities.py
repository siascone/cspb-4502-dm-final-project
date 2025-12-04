import pandas as pd
import matplotlib.pyplot as plotter

# --- Read in crash data csv files ---

# Crash Data by individual year
# crash_data = pd.read_csv('../assets/2021-Crash-Data-Normalized.csv') # 2021
# crash_data = pd.read_csv('../assets/2022-Crash-Data-Normalized.csv') # 2022
# crash_data = pd.read_csv('../assets/2023-Crash-Data-Normalized.csv') # 2023
# crash_data = pd.read_csv('../assets/2024-Crash-Data-Normalized.csv') # 2024

# All Crash Data 2021-2024
# NOTE: Follow instructions in readme to generate or retreive all_crash_data.csv
crash_data = pd.read_csv('../assets/all_crash_data.csv')
crash_data_frame = pd.DataFrame(crash_data) 



# --- Count of crashes analyzed---
num_crashes = crash_data["CUID"].count()



# --- Wild Animal, School Zone and Construciton Zone Related Crash Numbers ---
print("\n--- Wild Animal, School Zone and Construciton Zone Related Crash Numbers ---")

# Wild animal related crashes
num_wild_animal = crash_data["Wild Animal"].count()
wild_animal_prob_percent = (num_wild_animal / num_crashes ) * 100

print(f'Number of accidents involving a wild animal: {num_wild_animal}')
print(f'Probability of accident involving a wild animal: {wild_animal_prob_percent}')

# School zone related crashes
num_school_zone = crash_data["School Zone"].sum()
school_zone_prob_percent = (num_school_zone / num_crashes ) * 100

print(f'Number of accidents occuring in a School Zone: {num_school_zone}')
print(f'Probability of accident occuring in a School Zone: {school_zone_prob_percent}')

# Construction zone related crashes
num_construction_zone = crash_data["Construction Zone"].sum()
construction_zone_prob_percent = (num_construction_zone / num_crashes ) * 100

print(f'Number accidents occuring in a Construction Zone: {num_construction_zone}')
print(f'Probability of accident occuring in a Construction Zone: {construction_zone_prob_percent}')

# Plot Zone and Animal Related Probabilities
categories = ["Wild Animals", "School Zone", "Construction Zone"]
probs = [wild_animal_prob_percent, school_zone_prob_percent, construction_zone_prob_percent]

plotter.bar(categories, probs)
plotter.ylabel("Probability (%)")
plotter.title("Zone and Animal Related Crash Probabilities")
plotter.show()



# --- Weather related crashes ---
print("\n--- Weather Condition Related Crash Numbers ---")

# create weather conditions count DataFrame    
weather_condition_counts = crash_data_frame["Weather Condition"].value_counts()

# get counts accidents by weather conditions

# build lists of conditions and probabilites and print calculation
weather_conditions_lst = []
weather_condition_probs_lst = []

for condition, count in weather_condition_counts.items():
    weather_conditions_lst.append(condition)
    prob = (count / num_crashes) * 100
    weather_condition_probs_lst.append(prob)
    print(f'Probability of accident occurring when weather is {condition}: {prob}')

# plot weather conditions probs
plotter.bar(weather_conditions_lst, weather_condition_probs_lst)
plotter.ylabel("Probability (%)")
plotter.title("Weather Condition Crash Probabilities")
plotter.show()



# --- Location related crashes ---
print("\n--- Location Related Crash Numbers ---")

# get counts of accidents by location
location_crash_counts = crash_data_frame["System Code"].value_counts()

# build lists of locations and probabilites and print calculation
locations_lst = []
location_probs_lst = []

for location, count in location_crash_counts.items():
    locations_lst.append(location)
    prob = (count / num_crashes) * 100
    location_probs_lst.append(prob)
    print(f"Probability of accident occuring on {location}: {prob}")
        
# plot location probs
plotter.bar(locations_lst, location_probs_lst)
plotter.ylabel("Probability (%)")
plotter.title("Locations Crash Probabilities")
plotter.show()



# --- Road Condition related crashes ---
print("\n--- Road Condition Related Crash Numbers ---")

# get counts accidents by road condition
road_condition_counts = crash_data_frame["Road Condition"].value_counts()

# build lists of conditions and probabilites and print calculation
road_condition_lst = []
road_condition_probs_lst = []

for condition, count in road_condition_counts.items():
    road_condition_lst.append(condition)
    prob = (count / num_crashes) * 100
    road_condition_probs_lst.append(prob)
    print(f"Probability of accident occuring due to {condition}: {prob}")
        
# plot conditon probs
plotter.bar(road_condition_lst, road_condition_probs_lst)
plotter.ylabel("Probability (%)")
plotter.title("Road Condition Crash Probabilities")
plotter.show()



# --- Driver Action related crashes ---
print("\n--- Driver Action Related Crash Numbers ---")

# get counts accidents by driver action (condition)
driver_action_counts = crash_data_frame["Driver Action"].value_counts()

# build lists of actions and probabilites and print calculation
driver_action_lst = []
driver_action_probs_lst = []

for action, count in driver_action_counts.items():
    driver_action_lst.append(action)
    prob = (count / num_crashes) * 100
    driver_action_probs_lst.append(prob)
    print(f'Probability of accident occurring due to {action}: {prob}')

# plot action probs
plotter.bar(driver_action_lst, driver_action_probs_lst)
plotter.ylabel("Probability (%)")
plotter.title("Driver Action Crash Probabilities")
plotter.show()