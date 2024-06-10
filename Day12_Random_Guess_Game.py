import random
import os
from art import logo

print(logo)

def out():
    computer_random = random.randint(1,100)

    print("I am Thinking of a Number Between 1 to 100!!")

    option = input("Enter Difficulty Level 'Easy' or 'Hard'!! ")

    if option =='Easy':
        easy(computer_random)
    else:
        hard(computer_random)



def easy(number):
    tries = 10
    print("You have 10 Tries for Guessing the Number")

    while True:
        tries-=1
        user_number = int(input("Guess the Number "))
        if user_number > number:
            print("Too High")
            print(f"You have {tries} left")
        elif user_number < number:
            print("Too Low")
            print(f"You have {tries} left")
        else:
            print(f"On {tries} Try. You have Guessed the Correct Number which is {number}\n")
            break

        if tries==0:
            print("You have ZERO Tries Left and YOU HAVE LOST!!!!\n")
            break


    next = input("Do you want to play Again. Type 'Y' or 'N'\n")
    if next == 'Y':
        out()
    else:
        print("OKAY THANK YOU")
        


    
        
def hard(number):
    tries = 5
    print("You have 5 Tries for Guessing the Number")

    while True:
        tries-=1
        user_number = int(input("Guess the Number "))
        if user_number > number:
            print("Too High")
            print(f"You have {tries} left")
        elif user_number < number:
            print("Too Low")
            print(f"You have {tries} left")
        else:
            print(f"On {tries} Try. You have Guessed the Correct Number which is {number}\n")
            break

        if tries==0:
            print("You have ZERO Tries Left and YOU HAVE LOST!!!!\n")
            break    

    next = input("Do you want to play Again. Type 'Y' or 'N'\n")
    if next == 'Y':
        out()
    else:
        print("OKAY THANK YOU")


out()
