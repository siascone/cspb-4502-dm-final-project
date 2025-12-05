import constructionZoneAndDriverAction
import schoolZoneAndDriverAction
import wildAnimalAndDriverAction

import time

def main():
    
    running = True
    
    print("""
 >>> Crashing Through The Data <<<
 Exploring how Driver Action factors into School Zone, Construction Zone, 
 and Wild Animal related crashes under ideal conditions using Naïve Bayes 
 Classification.""")
    
    def print_choices():
        print("""
 -------------------------------
 Data Options to Explore:
 1. School Zone Crash Data
 2. Construction Zone Crash Data
 3. Wild Animal Crash Data
 4. Quit Program
 -------------------------------
        """)
            
    print_choices()
    
    while running:
        
        try:
            user_input = int(input(" Please make a selection: "))
        except ValueError:
            print(" ERROR: Pleas me sure your input is a number 1, 2, 3 or 4. \n")
            continue
                
        if (user_input == 1): 
            schoolZoneAndDriverAction.school_zone_report()
            # time.sleep(2.5)
            print_choices()
        elif (user_input == 2):
            constructionZoneAndDriverAction.construction_zone_report()
            # time.sleep(2.5)
            print_choices()
        elif (user_input == 3):
            wildAnimalAndDriverAction.wild_animal_report()
            # time.sleep(2.5)
            print_choices()
        elif (user_input == 4):
            running = False
        else:
            print(" You have entered an incorrect number please select 1, 2, 3 or 4")
            continue
            
    print("\n Thank you for exploring the data. Happy Mining!")
    
if __name__ == "__main__":
    main()