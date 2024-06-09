import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["chakwal", "punjab", "taxila"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


print(chosen_word)


lives =6

print(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives-=1
    if lives == 0:
        end_of_game = True
        print("You Lose")        


    

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print(stages[lives])













# import random
# words = ['hello','gym','lahore','taxila','islamabad','chakwal','tehman','stack']

# chosen_word = random.choice(words)

# word_length = len(chosen_word)

# print(chosen_word)

# display = []


# for _ in range(word_length):
#     display += "_"

# end = False


# while not end:
#     guess = input("Guess the Letter: ")


#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter

#     print(display)

#     if "_" not in display:
#         end = True
#         print("YO WON")

    

















# random_word = random.choice(words)

# print(random_word)
# guess = input("Guess a Letter: ")


# names = [*random_word]
# gg = len(random_word)



# while 


# bl = "_ "
# for a in random_word:
#     if a == guess:
#         print(a, end=" ")
#     else:
#         print(bl, end=" ")















