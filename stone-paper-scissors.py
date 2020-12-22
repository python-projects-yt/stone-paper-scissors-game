import random
random_generator = random.randint(1,3)



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


user_input = int(input("What do you want to choose  \n1) rock press 1 \n2) paper press 2 \n3) scissors press 3\n"))
# random_generator = random.randint(1,3)

if user_input == 1 and random_generator == 2:
    print("You Choose")
    print(rock)
    print("Computer Choose")
    print(paper)
    print("Computer Win!")
    print(paper)
    
elif user_input == 2 and random_generator == 1:
    print("You Choose")
    print(paper)
    print("Computer Choose")
    print(rock)

    print("You Win!")
    print(paper)
elif user_input == 2 and random_generator == 3:
    print("You Choose")
    print(paper)
    print("Computer Choose")
    print(scissors)

    print("Computer Win!")
    print(scissors)
elif user_input == 3 and random_generator == 2:
    print("You Choose")
    print(scissors)
    print("Computer Choose")
    print(paper)

    print("You Win!")
    print(scissors)    
elif user_input == 1 and random_generator == 3:
    print("You Choose")
    print(rock)
    print("Computer Choose")
    print(scissors)

    print("You Win!")
    print(rock)
elif user_input == 3 and random_generator == 1:
    print("You Choose")
    print(scissors)
    print("Computer Choose")
    print(rock)

    print("Computer Win!")
    print(rock)        

print('=========================================================')  

