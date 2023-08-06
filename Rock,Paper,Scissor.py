import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors]

me=int(input('Whats your choice. Choose 0 for rock, 1 for paper and 2 for scissors? '))

print(game[me])

computer=random.randint(0,2)

print(f"Computer choice is {computer}")

print(game[computer])

# IF STATEMENTS:

if me==0 and computer==1:
    print("Computer wins")
elif me==0 and computer ==2:
    print("You Win")
elif me==1 and computer==0:
    print('Your win')
elif me==1 and computer==2:
    print('Computer wins')
elif me==2 and computer==0:
    print("Computer wins")
elif me==2 and computer==1:
    print("You Win")
elif me==computer:
    print("ITS A DRAW")
