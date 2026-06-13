import random
rock='''
    _______
---'________)
      (______)
      (______)
      (_____)
---.__(___)
'''
paper='''
     _______
---'__________)____
     ______________)
        __________)
      ___________)
---.___________)
     '''
scissors='''
     _______
---'     ____)_______
           __________)
         ______________)
        (______)
---.---(____)
'''
game_images=[rock,paper,scissors]
print(game_images[0])
print(game_images[1])
print(game_images[2])
your_choice=int(input("What do you choose? 0 for Rock,1 for paper or 2 for Scissors:"))
#012
if(your_choice>=0 and your_choice<=2):
    print(game_images[your_choice])
computer_choice=random.randint(0,2)
print(f"computer chooses {game_images[computer_choice]}")
if(your_choice==0 and computer_choice==2):
    print("You win")
elif(your_choice==2 and computer_choice==0):
    print("You lose")
elif(computer_choice>your_choice):
    print("You lose!")
elif(your_choice>computer_choice):
    print("You win!")
elif(your_choice==computer_choice):
    print("its a draw")
else:
    print("you entered a wrong choice")

