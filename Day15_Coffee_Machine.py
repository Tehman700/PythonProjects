import random
import os

water = 300
coffee = 100
milk = 200
money =0


def refil():
    global water,coffee,milk
    water =300
    coffee=100
    milk =200
    print("TANK HAS BEEN REFILLED!!!")



def espresso():
    global water, coffee, milk, money
    espresso_water = 50
    espresso_coffee = 18
    espresso_price = 1.50

    if water >= espresso_water and coffee >= espresso_coffee:
        print("Please Insert Coins\n")
        qq = float(input("How many Quarters?: "))
        di = float(input("How many Dimes?: "))
        ni = float(input("How many Nickels?: "))
        pen = float(input("How many Pennies?: "))

        sum_of_money = float(((0.25 * qq) + (0.10 * di) + (0.05 * ni) + (0.01 * pen)))
        if sum_of_money >= espresso_price:
            change = sum_of_money - espresso_price
            print(f"Here is ${round(change, 2)} in change")
            print("Here is Your Espresso")
            
            water -= espresso_water
            coffee -= espresso_coffee
            money += espresso_price

        else:
            print("You don't have enough money")
    else:
        print("RESOURCES ARE NOT ENOUGH!!!")



def latte():
    global water, coffee, milk, money
    latte_water = 200
    latte_coffee = 24
    latte_price = 2.50
    latte_milk = 150

    if water >= latte_water and coffee >= latte_coffee and milk >= latte_milk:
        print("Please Insert Coins\n")
        qq = float(input("How many Quarters?: "))
        di = float(input("How many Dimes?: "))
        ni = float(input("How many Nickels?: "))
        pen = float(input("How many Pennies?: "))

        sum_of_money = float(((0.25 * qq) + (0.10 * di) + (0.05 * ni) + (0.01 * pen)))
        if sum_of_money >= latte_price:
            change = sum_of_money - latte_price
            print(f"Here is ${round(change, 2)} in change")
            print("Here is Your Latte")
            
            water -= latte_water
            coffee -= latte_coffee
            money += latte_price

        else:
            print("You don't have enough money")
    else:
        print("RESOURCES ARE NOT ENOUGH!!!")

def cappucino():
    global water, coffee, milk, money
    c_water = 250
    c_coffee = 24
    c_price = 3.00
    c_milk = 100

    if water >= c_water and coffee >= c_coffee and milk >= c_milk:
        print("Please Insert Coins\n")
        qq = float(input("How many Quarters?: "))
        di = float(input("How many Dimes?: "))
        ni = float(input("How many Nickels?: "))
        pen = float(input("How many Pennies?: "))

        sum_of_money = float(((0.25 * qq) + (0.10 * di) + (0.05 * ni) + (0.01 * pen)))
        if sum_of_money >= c_price:
            change = sum_of_money - c_price
            print(f"Here is ${round(change, 2)} in change")
            print("Here is Your Cappuccino")
            
            water -= c_water
            coffee -= c_coffee
            money += c_price

        else:
            print("You don't have enough money")
    else:
        print("RESOURCES ARE NOT ENOUGH!!!")




def report():
    global water,milk,coffee,money
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")    





while True:
    option = input("What would you like? (espresso/latte/cappuccino/report/exit): ")
    if option == "espresso":
        espresso()
    elif option == "latte":
        latte()
    elif option == "cappuccino":
        cappucino()
    elif option == "report":
        report()
    elif option == "exit":
        break
    elif option == "refill":
        refil()

    else:
        print("You have chosen Wrong Option")