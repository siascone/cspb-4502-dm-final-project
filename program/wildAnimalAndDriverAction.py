import pandas as pd

def wild_animal_report():
    # Read in crash data
    crash_data = pd.read_csv("../assets/all_crash_data.csv")
    crash_data_frame = pd.DataFrame(crash_data)
    
    print("\n ----------------------------------------------------------------------------")
    print(" >>> Classifier Driver Action in Wild Animal Crash Under Ideal Conditions <<< \n")

    # count num crashes and set up data frame
    num_crashes = crash_data["CUID"].count()

    # count num crashes involving a wild animal
    num_animal_crashes = crash_data["Wild Animal"].count()
    prob_animal_crashes = (num_animal_crashes / num_crashes)

    print(" --- Some General Numbers --- \n")

    print(f" Number of crashes Analyzed: {num_crashes}")
    print(f" Number of crashes involving a Wild Animal: {num_animal_crashes}")
    print(f" Probability of a crash involving a Wild Animal: {prob_animal_crashes}\n")

    print(" --- Classifier and Scenerio --- \n")

    print(""" Classifier Driver Action:
    C1 = No Contributing Action
    C2 = Contributing Action

    Wild Animal Crash Under Ideal Conditions:
    X = [Weather Condition: Clear, Road Condition: Dry, Wild Animal: True] \n""")

    # Calculate counts and probs of C1 and C2
    print(" --- Probabilities of C1 & C2 --- \n")

    num_nca = crash_data_frame["Driver Action"].value_counts().get("No Contributing Action")
    prob_nca = (num_nca / num_crashes)

    num_ca = num_crashes - num_nca
    prob_ca = (num_ca / num_crashes)

    print(f" P(C1) = P(No Contributing Factor): {prob_nca}")
    print(f" P(C2) = P(Contributing Factor): {prob_ca}\n")

    # Calculate probs of Wild Animal against C1 & C2
    print(" --- Probability Wild Animal against C1 & C2 --- \n")

    num_animal_nca = crash_data_frame[crash_data_frame["Driver Action"] == "No Contributing Action"]["Wild Animal"].value_counts().sum()
    prob_animal_nca = (num_animal_nca / num_nca)

    num_animal_ca = crash_data_frame[crash_data_frame["Driver Action"] != "No Contributing Action"]["Wild Animal"].value_counts().sum()
    prob_animal_ca = (num_animal_ca / num_ca)

    print(f" P(Wild Animal | No Contributing Factor): {prob_animal_nca}")
    print(f" P(Wild Animal | Contributing Factor): {prob_animal_ca} \n")

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

    prob_x_nca = (prob_animal_nca * prob_clear_nca * prob_dry_nca)
    prob_x_ca = (prob_animal_ca * prob_clear_ca * prob_dry_ca)

    print(f" P(X | No Contributing Action): {prob_x_nca}")
    print(f" P(X | Contributing Action): {prob_x_ca} \n")

    # Calculate Naïve Bayesian Classifier Determination
    print(" --- Naïve Bayesian Classifier Determination --- \n")

    prob_x_nca_prob_nca = prob_x_nca * prob_nca
    prob_x_ca_prob_ca = prob_x_ca * prob_ca

    print(f" P(X | No Contributing Action) * P(No Contributing Action): {prob_x_nca_prob_nca}")
    print(f" P(X | Contributing Action) * P(Contributing Action): {prob_x_ca_prob_ca} \n")

    if (prob_x_nca_prob_nca > prob_x_ca_prob_ca):
        print(" RESULT: Given the crash senerio X = [Weather Condition: Clear, Road Condition: Dry, Wild Animal: True] we predict there will be No Contributing Action from the driver.")
    else:
        print(" RESULT: Given the crash senerio X = [Weather Condition: Clear, Road Condition: Dry, Wild Animal: True] we predict there will be a Contributing Action from the driver.")
