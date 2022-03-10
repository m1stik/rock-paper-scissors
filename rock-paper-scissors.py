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

#Input
choose = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

pc_choose = random.randint(0,2)

#Player turn
if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
else:
    print(scissors)

#Computer turn
print("Computer chose:\n")

if pc_choose == 0:
    print(rock)
elif pc_choose == 1:
    print(paper)
else:
    print(scissors)

#Game logic and result
if choose == 0 and pc_choose == 0:
    print("Draw")
elif choose == 1 and pc_choose == 0:
    print("Win!")
elif choose == 2 and pc_choose == 0:
    print("You lose")
elif choose == 0 and pc_choose == 1:
    print("You lose")
elif choose == 1 and pc_choose == 1:
    print("Draw")
elif choose == 2 and pc_choose == 1:
    print("Win!")
elif choose == 0 and pc_choose == 2:
    print("Win!")
elif choose == 1 and pc_choose == 2:
    print("You lose")
elif choose == 2 and pc_choose == 2:
    print("Draw")