import pandas as pd
import matplotlib.pyplot as plotter


# Read in crash data
crash_data = pd.read_csv("assets/all_crash_data.csv")
crash_data_frame = pd.DataFrame(crash_data)

# Title Header
print("--- Crash Data: Wild Animals and Driver Actions in ideal conditions ---\n")

# Basic counts/probs header
print("--- Counts and Individual Probabilities ---\n")

# Calculate number of crash reports
num_crashes = crash_data["CUID"].count()
print(f"Number of crashes analyzed: {num_crashes}\n")

# Count nubmer of crashes involving a Wild Animal
# NOTE: reports not involving wild animals are empty in this column
#       Wild animal reported by name (Deer, Fox, Moose, etc.)
num_wild_animal_crashes = crash_data["Wild Animal"].count()
print(f"Number of crashes involving a Wild Animal: {num_wild_animal_crashes}\n")

# Determin if Driver Action plays a significant role in Wild Animal related 
# crashes in otherwise ideal conditions 
# - Scenerio = (Weather: Clear, Road: Dry, Zone: Wild Animal)
# - C1 = No Contributing Action, 
# - C2 = Contributing action (Careless Driving, Speeding, etc.)

# Count of crashes innvolving no contributing action from driver
num_nca = crash_data_frame["Driver Action"].value_counts().get("No Contributing Action")
print(f"Number of crashes with No Contributing Action from Driver: {num_nca}")
# Calculate P(No Contributing Action)
prob_nca = (num_nca / num_crashes)
print(f"    Probability of NCA: {prob_nca}\n")

# Count of crashes involving contributing action from driver 
num_ca = num_crashes - num_nca
print(f"Number of crashes with Contributing Action from Driver: {num_ca}")
# Calculate P(Contributing Action)
prob_ca = (num_ca / num_crashes)
print(f"    Probability of CA: {prob_ca}\n")

# Count of crashes with Clear Weather Conditions
num_clear = crash_data_frame["Weather Condition"].value_counts().get("Clear")
print(f"Number of crashes with Clear Weather Conditions: {num_clear}")
prob_clear = (num_clear / num_crashes)
print(f"    Probability of Clear Weather Conditions: {prob_clear}\n")

# Count of crashes with Dry Road Conditions
num_dry = crash_data_frame["Road Condition"].value_counts().get("Dry")
print(f"Number of crashes with Dry Road Conditions: {num_dry}")
prob_dry = (num_dry / num_crashes)
print(f"    Probability of Dry Road Conditions: {prob_dry}\n")

# --- Wild Animal and Driver Action ---

print("--- Wild Animal and Driver Action Probability ---\n")

# Animal and No Contributing Action
num_animal_nca = crash_data_frame[crash_data_frame["Driver Action"] == "No Contributing Action"]["Wild Animal"].value_counts().sum()
print(f"Number of crashes involving an animal with No Contributing Action from driver: {num_animal_nca}")
prob_animal_nca = (num_animal_nca / num_nca)
print(f"    Probability of Animal and No Contribuitng Action from driver: {prob_animal_nca}\n")


# Animal and Contributing Action
num_animal_ca = crash_data_frame[crash_data_frame["Driver Action"] != "No Contributing Action"]["Wild Animal"].value_counts().sum()
print(f"Number of crashes involving an animal with Contributing Action from driver: {num_animal_ca}")
prob_animal_ca = (num_animal_ca / num_ca)
print(f"    Probability of Animal and Contribuitng Action from driver: {prob_animal_ca}\n")


# --- Clear Weather and Driver Action ---

print("--- Clear Weather and Driver Action Probability ---\n")

# Clear weather and No Contributing Action
num_clear_nca = crash_data_frame[crash_data_frame["Driver Action"] == "No Contributing Action"]["Weather Condition"].value_counts().get("Clear")
print(f"Number of crashes under Clear Weather Conditions with No Contributing Action from Driver: {num_clear_nca}")
prob_clear_nca = (num_clear_nca / num_nca)
print(f"    Probability of crash under Clear Weather Conditions with No Contributing Action from Driver: {prob_clear_nca}\n")

# Clear weather and Contributing Action
num_clear_ca = crash_data_frame[crash_data_frame["Driver Action"] != "No Contributing Action"]["Weather Condition"].value_counts().get("Clear")
print(f"Number of crashes under Clear Weather Conditions with Contributing Action from Driver: {num_clear_ca}")
prob_clear_ca = (num_clear_ca / num_ca)
print(f"    Probability of crash under Clear Weather Conditions with Contributing Action from Driver: {prob_clear_ca}\n")


# --- Dry Roads and Driver Action ---

print("--- Dry Roads and Driver Action Probability ---\n")

# Dry Roads and No Contributing Action
num_dry_nca = crash_data_frame[crash_data_frame["Driver Action"] == "No Contributing Action"]["Road Condition"].value_counts().get("Dry")
print(f"Number of crashes under Dry Road Conditions with No Contributing Action from Driver: {num_dry_nca}")
prob_dry_nca = (num_dry_nca / num_nca)
print(f"    Probability of crash under Dry Road Conditions with No Contributing Action from Driver: {prob_dry_nca}\n")

# Dry Roads and Contributing Action
num_dry_ca = crash_data_frame[crash_data_frame["Driver Action"] != "No Contributing Action"]["Road Condition"].value_counts().get("Dry")
print(f"Number of crashes under Dry Road Conditions with Contributing Action from Driver: {num_dry_ca}")
prob_dry_ca = (num_dry_ca / num_ca)
print(f"    Probability of crash under Dry Road Conditions with Contributing Action from Driver: {prob_dry_ca}\n")

# --- Naïve Bayesian Classifier of X Conditions and Driver Actions ---
print("--- Naïve Bayesian Classifier of X Conditions and Driver Actions ---")
print("    X Conditions = [Weather: Clear, Roads: Dry, Zone: Animal]\n")

# Calculate P(X | No Contributing Action)
prob_x_nca = (prob_animal_nca * prob_clear_nca * prob_dry_nca)
print(f"P(X | No Contributing Action): {prob_x_nca}")

# Calculate P(X | Contributing Action)
prob_x_ca = (prob_animal_ca * prob_clear_ca * prob_dry_ca)
print(f"P(X | Contributing Action): {prob_x_ca}\n")

print("Naïve Bayesian Classifier Determination")
# Calculate P(X | No Contributing Action)* P(No Contributing Action)
prob_x_nca_prob_nca = prob_x_nca * prob_nca
print(f"P(X | No Contributing Action)*P(No Contributing Action): {prob_x_nca_prob_nca}")

prob_x_ca_prob_ca = prob_x_ca * prob_ca
print(f"P(X | Contributing Action)*P(Contributing Action): {prob_x_ca_prob_ca} \n")

if (prob_x_nca_prob_nca > prob_x_ca_prob_ca):
    print("Given the crash senerio X = [Weather: Clear, Roads: Dry, Wild Animal: True] it is most probable that there will be No Contributing Action from the driver.")
else:
    print("Given the crash senerio X = [Weather: Clear, Roads: Dry, Wild Animal: True] it is most probable that there will be a Contributing Action from the driver.")