import pandas as pd

def school_zone_report():
    # Read in crash data
    crash_data = pd.read_csv("../assets/all_crash_data.csv")
    crash_data_frame = pd.DataFrame(crash_data)
    print("\n ----------------------------------------------------------------------------")
    print(" >>> Classifier Driver Action in School Zone Crash Under Ideal Conditions <<< \n")

    # count num crashes and set up data frame
    num_crashes = crash_data["CUID"].count()

    # count num crashes involving a wild animal
    num_school_crashes = crash_data["School Zone"].sum()
    prob_school_crashes = (num_school_crashes / num_crashes)

    print(" --- Some General Numbers --- \n")

    print(f" Number of crashes Analyzed: {num_crashes}")
    print(f" Number of crashes in a School Zone: {num_school_crashes}")
    print(f" Probability of a crash in a School Zone: {prob_school_crashes}\n")

    print(" --- Classifier and Scenerio --- \n")

    print(""" Classifier Driver Action:
    C1 = No Contributing Action
    C2 = Contributing Action

    School Zone Crash Under Ideal Conditions:
    X = [Weather Condition: Clear, Road Condition: Dry, School Zone: True] \n""")

    # Calculate counts and probs of C1 and C2
    print(" --- Probabilities of C1 & C2 --- \n")

    num_nca = crash_data_frame["Driver Action"].value_counts().get("No Contributing Action")
    prob_nca = (num_nca / num_crashes)

    num_ca = num_crashes - num_nca
    prob_ca = (num_ca / num_crashes)

    print(f" P(C1) = P(No Contributing Factor): {prob_nca}")
    print(f" P(C2) = P(Contributing Factor): {prob_ca}\n")

    # Calculate probs of School Zone against C1 & C2
    print(" --- Probability School Zone against C1 & C2 --- \n")

    num_school_nca = crash_data_frame[crash_data_frame["Driver Action"] == "No Contributing Action"]["School Zone"].value_counts().get(True)
    prob_school_nca = (num_school_nca / num_nca)

    num_school_ca = crash_data_frame[crash_data_frame["Driver Action"] != "No Contributing Action"]["School Zone"].value_counts().get(True)
    prob_school_ca = (num_school_ca / num_ca)

    print(f" P(School Zone | No Contributing Factor): {prob_school_nca}")
    print(f" P(School Zone | Contributing Factor): {prob_school_ca} \n")

    # Calculate probs of Clear Weather Conditions against C1 & C2
    print(" --- Probability Clear Weather Conditions against C1 & C2 --- \n")

    num_clear_nca = crash_data_frame[crash_data_frame["Driver Action"] == "No Contributing Action"]["Weather Condition"].value_counts().get("Clear")
    prob_clear_nca = (num_clear_nca / num_nca)

    num_clear_ca = crash_data_frame[crash_data_frame["Driver Action"] != "No Contributing Action"]["Weather Condition"].value_counts().get("Clear")
    prob_clear_ca = (num_clear_ca / num_ca)

    print(f" P(Clear Weather | No Contributing Factor): {prob_clear_nca}")
    print(f" P(Clear Weather | Contributing Factor): {prob_clear_ca} \n")

    # Calculate probs of Dry Road Conditions against C1 & C2
    print(" --- Probability Dry Road Conditions against C1 & C2 --- \n")

    num_dry_nca = crash_data_frame[crash_data_frame["Driver Action"] == "No Contributing Action"]["Road Condition"].value_counts().get("Dry")
    prob_dry_nca = (num_dry_nca / num_nca)

    num_dry_ca = crash_data_frame[crash_data_frame["Driver Action"] != "No Contributing Action"]["Road Condition"].value_counts().get("Dry")
    prob_dry_ca = (num_dry_ca / num_ca)

    print(f" P(Dry Roads | No Contributing Factor): {prob_dry_nca}")
    print(f" P(Dry Roads | Contributing Factor): {prob_dry_ca} \n")

    # Calculate prob of X against C1 & C2
    print(" --- Probability of Senerio X against C1 & C2 --- \n")

    prob_x_nca = (prob_school_nca * prob_clear_nca * prob_dry_nca)
    prob_x_ca = (prob_school_ca * prob_clear_ca * prob_dry_ca)

    print(f" P(X | No Contributing Action): {prob_x_nca}")
    print(f" P(X | Contributing Action): {prob_x_ca} \n")

    # Calculate Naïve Bayesian Classifier Determination
    print(" --- Naïve Bayesian Classifier Determination --- \n")

    prob_x_nca_prob_nca = prob_x_nca * prob_nca
    prob_x_ca_prob_ca = prob_x_ca * prob_ca

    print(f" P(X | No Contributing Action) * P(No Contributing Action): {prob_x_nca_prob_nca}")
    print(f" P(X | Contributing Action) * P(Contributing Action): {prob_x_ca_prob_ca} \n")

    if (prob_x_nca_prob_nca > prob_x_ca_prob_ca):
        print(" RESULT: Given the crash senerio X = [Weather Condition: Clear, Road Condition: Dry, School Zone: True] we predict there will be No Contributing Action from the driver.")
    else:
        print(" RESULT: Given the crash senerio X = [Weather Condition: Clear, Road Condition: Dry, School Zone: True] we predict there will be a Contributing Action from the driver.")
