import os




while True:
    
    print("==================================")
    print("Welcome to my Currency and Weight Converter. Please choose an option below:")
    print("----------------------------------")
    print("1. Convert currency ($ - Euro - Yen)")
    print("2. Convert weight (kg - pound)")
    print("3. Convert measurement (cm - inch)")
    print("4. Exit")
    print("5.clear screen")
    print("===================================")

    user_choose = input("Enter your option number here: ").strip()
    
    if user_choose not in ["1", "2", "3", "4","5"]:
        print("❌ Enter a valid number!")
        continue

    if user_choose == "1":
       
        while True:
            print("Available conversions:")
            print("=========================")
            print(" - dollar to yen")
            print(" - dollar to euro")
            print(" - yen to dollar")
            print(" - yen to euro")
            print(" - euro to yen")
            print(" - euro to dollar")
            print("=========================")
            chose_currency = input("Choose your currency conversion (e.g. dollar to yen): ").strip().lower()
            try:
                chose_amount = float(input("Enter your amount of the currency: "))
            except ValueError:
                print("❌ Invalid amount! Please enter a number.")
                continue
            
            if chose_currency == "dollar to yen":
                new_value = chose_amount * 148
                print(f"{chose_amount} USD is equal to {new_value} Japanese Yen.")
            elif chose_currency == "dollar to euro":
                new_value = chose_amount * 0.86
                print(f"{chose_amount} USD is equal to {new_value} Euro.")
            elif chose_currency == "yen to dollar":
                new_value = chose_amount * 0.01
                print(f"{chose_amount} Japanese Yen is equal to {new_value} USD.")
            elif chose_currency == "yen to euro":
                new_value = chose_amount * 0.01
                print(f"{chose_amount} Japanese Yen is equal to {new_value} Euro.")
            elif chose_currency == "euro to yen":
                new_value = chose_amount * 172
                print(f"{chose_amount} Euro is equal to {new_value} Japanese Yen.")
            elif chose_currency == "euro to dollar":
                new_value = chose_amount * 1.17
                print(f"{chose_amount} Euro is equal to {new_value} USD.")
            else:
                print("❌ Wrong input, please choose a valid conversion.")
            redo = input("Do you want to convert another currency?:[y/n]").strip().lower()
            if redo =="y":
                continue
            else:
                print("returning to main menu . . .")
                break                    
    elif user_choose == "2":
       while True:
            user_choice = input("Choose to convert (kg-pound or pound-kg): ").strip().lower()
            try:
                user_weight = float(input("Enter your weight: "))
            except ValueError:
                print("❌ Invalid weight! Please enter a number.")
                continue
            
            if user_choice == "kg-pound":
                pound = user_weight * 2.204623
                print(f"{user_weight} kilograms is equal to {pound} pounds.")
            elif user_choice == "pound-kg":
                kg = user_weight * 0.453592
                print(f"{user_weight} pounds is equal to {kg} kilograms.")
            else:
                print("❌ Wrong input, please choose a valid conversion.")

            redo = input("Do you want to convert another currency?:[y/n]").strip().lower()
            if redo =="y":
                continue
            else:
                print("returning to main menu . . .")
                break        

    elif user_choose == "3":
        while True:
            user_choice = input("Choose to convert (cm-inch or inch-cm): ").strip().lower()
            try:
                user_measure = float(input("Enter your measurement: "))
            except ValueError:
                print("❌ Invalid measurement! Please enter a number.")
                continue
            
            if user_choice == "cm-inch":
                inch = user_measure * 0.393701
                print(f"{user_measure} cm is equal to {inch} inches.")
            elif user_choice == "inch-cm":
                cm = user_measure * 2.54
                print(f"{user_measure} inches is equal to {cm} cm.")
            else:
                print("❌ Wrong input, please choose a valid conversion.")

            redo = input("Do you want to convert another currency?:[y/n]").strip().lower()
            if redo =="y":
                continue
            else:
                print("returning to main menu . . .")
                break        
    elif user_choose =="5":
        os.system('cls')
        continue

    elif user_choose == "4":
        print("Thanks for using my app. Goodbye! 👋")
        break

