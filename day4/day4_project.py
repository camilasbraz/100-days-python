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

import random

ascii_images = [rock, paper, scissors]
human_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
print("You chose:")
print(ascii_images[int(human_choice)])

pc_choice = random.randint(0,2)
print("Computer chose:")
print(ascii_images[pc_choice])

# rock(0) beats scissors(2)
# scissors(2) beat paper(1)
# paper(1) beats rock(0)
# tie

if human_choice == pc_choice:
    print("Tie!")

else:
    if pc_choice == 0 :
        if human_choice == 1:
            print("You win")
        else:
            print("You lose")
    
    if pc_choice == 1:
        if human_choice == 0:
            print("You lose")
        else:
            print("You win")

    if pc_choice == 2:
        if human_choice == 0:
            print("You win")
        else:
            print("You lose")
