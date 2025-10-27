import random
while True:
    com_guess = random.randint(1,100)

    while True:
        num = int(input("Enter a number between 1 to 100: "))
        if num<com_guess:
            print("Guess high")
        elif num>com_guess:
            print("Guess low")
        else:
            print("You got it")
            break

    con = input("Do you want to play again? (y/n)")
    if(con == 'n' or con == 'N'):
        exit()
