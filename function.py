import sys
import os

from coins import USD, ILS, EUR

# The class receives 2 variables of what to convert and how much to convert and stores values inside the list
class Resulta:
    def __init__(self, value, flow):
        self.value = value
        self.flow = flow

    def convert_and_store(value, flow, results_list):
        result = Resulta(value, flow)
        if flow == '1':
             new = f"{USD.calculate(value)}+','+ 'USD to ILS'"
        if flow == '2':
             new = f"{ILS.calculate(value)}+','+ 'ILS to USD'"
        if flow == '3':
             new = f"{EUR.calculate(value)}+','+ 'EURO to ILS'"
        results_list.append(new)



# The opening screen and input value
def start_over(results):
    print("Please choose an option (1/2/3):")
    print("1. Dollars to Shekels")
    print("2. Shekels to Dollars")
    print("3. Euro to Shekels")

    choice = input("Enter your choice (1/2/3): ")
    get_user_value(choice, results)

# Choosing whether to continue or not
def yes_or_no(continue_yn, result):
# If so we will return to the beginning of the program
    if continue_yn == "y":
        start_over(result)
# If not then we will print values and exit the program
    elif continue_yn == "n":
        file_result = open('C:\\Users\\Refael\\Desktop\\result.txt', 'w')
        for i in result:
            file_result.write(f"{i}\n")
        print(result)
        print("thank you")
        os.startfile("C:\\Users\\Refael\\Desktop\\result.txt")  # open the file using the default application
        sys.exit()
    else:
        print("Invalid choice. Please enter y or n.")
        x = input('choose y to start over or n to get out')
        yes_or_no(x, result)

# We will check what the selected number is and according to it we will convert the money
def get_user_value(user_choice, result):
    if user_choice == '1':
        dollars = float(input('please enters an amount to convert'))
        if dollars <= 0:
            print("write a number big then 0")
            get_user_value(user_choice, result)
        usd = USD()
        result.append(f"{USD.calculate(dollars)}+','+ 'USD to ILS'")
        print(f"{dollars} dollars = {usd.calculate(dollars)} shekels")
        x = input('choose y to start over or n to get out')
        yes_or_no(x, result)
    elif user_choice == '2':
        shekels = float(input('please enter an amount to convert'))
        if shekels <= 0:
            print("write a number big then 0")
            get_user_value(user_choice, result)
        ils = ILS()
        result.append(f"{ILS.calculate(shekels)}+','+ 'ILS to USD'")
        print(f"{shekels} shekels = {ils.calculate(shekels)} dollars")
        x = input('choose y to start over or n to get out')
        yes_or_no(x, result)
    elif user_choice == '3':
        euro = float(input('please enter an amount to convert'))
        if euro <= 0:
            print("write a number big then 0")
            get_user_value(user_choice, result)
        eur = EUR()
        result.append(f"{EUR.calculate(euro)}+','+ 'EURO to ILS'")
        print(f"{euro} euro = {eur.calculate(euro)} shekels")
        x = input('choose y to start over or n to get out')
        yes_or_no(x, result)
    else:
        print("Invalid Choice, please try again")
        start_over(result)