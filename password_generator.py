import random

# List of characters to use in the password
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# Getting user input
alpha = int(input("How many characters do you want? "))
num = int(input("How many numbers do you want? "))
sym = int(input("How many symbols do you want? "))

# Initialize an empty string
n = ""

# Add random alphabetic characters
for char in range(alpha):
    n += random.choice(alphabet)

# Add random numbers
for char in range(num):
    n += random.choice(numbers)

# Add random symbols
for char in range(sym):
    n += random.choice(symbols)
print(n)


# Convert the string to a list of characters and shuffle it
n_list = list(n)
random.shuffle(n_list)

# Join the shuffled list back into a string
final_password = ''.join(n_list)

# Print the final password
print(final_password)
