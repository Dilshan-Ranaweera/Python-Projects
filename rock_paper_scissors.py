import random
choices = ["Rock", "Paper", "Scissors"]
print("Rock Paper Scissors")
def select_player_choice(choice):
    if(choice == 1):
        return 'Rock'
    elif (choice == 2):
        return 'Paper'
    else:
        return 'Scissors'
    
def find_winner(comp,user):
    if(comp == user):
        print("It’s a draw 🤝")
    elif (comp == 'Rock' and user == 'Paper'):
        print("You win 🏆")
    elif (comp == 'Paper' and user == 'Scissors'):
        print("You win 🏆")
    elif (comp == 'Scissors' and user == 'Rock'):
        print("You win 🏆")
    else:
        print("You lose")


while True:
    print("1 - 🪨  Rock")
    print("2 - 📄 Paper")
    print("3 - ✂️  Scissors")
    com_choice = random.choice(choices)
    
    try:
        temp = int(input("Enter your choice: (1,2,3)"))
        if temp not in (1,2,3):
            print("Select a number between 1 to 3")
            continue
    except ValueError:
        print("Invalid input. Please select a number between 1 to 3")
        continue
    
    user_choice = select_player_choice(temp)
    find_winner(com_choice,user_choice)

    play = input("Do you want to play again: (y/n)")
    if (play == 'n' or play == 'N'):
        print("Terminate..")
        break
    