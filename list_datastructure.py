import random

nn = input("Enter the names of People \n")

names = nn.split(", ")

new = len(names)

# len() returns the total number of items in a list


new_f = random.randint(0,new-1)


new_f = random.random()

print(names[new_f]+ " is going to Pay the Bill Today!!")



fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])