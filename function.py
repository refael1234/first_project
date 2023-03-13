import sys
import os

from coins import USD, ILS, EUR


def start_over(results):
    print("Please choose an option (1/2/3):")
    print("1. Dollars to Shekels")
    print("2. Shekels to Dollars")
    print("3. Euro to Shekels")

    choice = input("Enter your choice (1/2/3): ")
    get_user_value(choice, results)

def yes_or_no(continue_yn, result):
    if continue_yn == "y":
        start_over(result)
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


def get_user_value(user_choice, result):
    if user_choice == '1':
        dollars = float(input('please enters an amount to convert'))
        if dollars <= 0:
            print("write a number big then 0")
            get_user_value(user_choice, result)
        usd = USD()
        result.append(f"{dollars} dollars = {usd.calculate(dollars)} shekels")
        print(f"{dollars} dollars = {usd.calculate(dollars)} shekels")
        x = input('choose y to start over or n to get out')
        yes_or_no(x, result)
    elif user_choice == '2':
        shekels = float(input('please enter an amount to convert'))
        if shekels <= 0:
            print("write a number big then 0")
            get_user_value(user_choice, result)
        ils = ILS()
        result.append(f"{shekels} shekels = {ils.calculate(shekels)} dollars")
        print(f"{shekels} shekels = {ils.calculate(shekels)} dollars")
        x = input('choose y to start over or n to get out')
        yes_or_no(x, result)
    elif user_choice == '3':
        euro = float(input('please enter an amount to convert'))
        if euro <= 0:
            print("write a number big then 0")
            get_user_value(user_choice, result)
        eur = EUR()
        result.append(f"{euro} euro = {eur.calculate(euro)} shekels")
        print(f"{euro} euro = {eur.calculate(euro)} shekels")
        x = input('choose y to start over or n to get out')
        yes_or_no(x, result)
    else:
        print("Invalid Choice, please try again")
        start_over(result)