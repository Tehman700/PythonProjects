import random
import os

list = {
}





def entering():
    while True:
        key = input("Enter Name of Bidder: ")
        value =int(input("Enter amount you want to Bid: "))
        list[key] = value
        highest = 0
        if value > highest:
            highest = value
        
        


        option = input("Is there any other Bidder\n'yes'\n'no'\n")
        if option != 'yes':
            os.system('cls')
            print(f"The highest Bidder Bid is of {key} and amount is {highest}")
            break

        else:
            os.system('cls')







entering()




# def enter_data():
#     data = {}
#     while True:
#         key = input("Enter key (or 'done' to finish): ")
#         if key.lower() == 'done':
#             break
#         value = input(f"Enter value for {key}: ")
#         data[key] = value
#     return data

# Using the function
# my_data = enter_data()
