
import random
player_choice = "y" 

while player_choice == "y" or player_choice == "Y" :
    print("Start Game ")
    print("1. Rock")
    print("2. Paper ")
    print("3. Scissors ")
    player = int(input("What do you want to throw? "))
    computer = random.randint(1,3)

    if player == 1:
        choice = "Rocks"
    elif player == 2:
        choice = "Paper"
    elif player == 3:
        choice = "Scissors"

    if computer == 1:
        choices = "Rocks"
    elif computer == 2:
        choices = "Paper"
    elif computer == 3:
        choices = "Scissors"

    print ("Computer: ", choices, " vs You: ", choice)

    if player == 1 and computer == 3:
        print("You win!")
    elif player == 2 and computer == 1:
        print("You win!")
    elif player == 3 and computer == 2:
        print("You win!")

    elif player == 1 and computer == 1:
        print("It's a tie!")
    elif player == 2 and computer == 2:
        print("It's a tie!")
    elif player == 3 and computer == 3:
        print("It's a tie!")

    elif computer == 1 and player == 3:
        print("You lose!")
    elif computer == 2 and player == 1:
        print("You lose!")
    elif computer == 3 and player == 2:
        print("You lose!")
    player_choice = input("Do you want to play again(y/n)? ")
    
    
print("Thank you!")
