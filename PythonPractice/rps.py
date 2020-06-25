
while(allow):
    gamedict = {"rock" : 1, "paper" : 2, "scissors" : 3}
    print("Choose One: Rock, Paper, Scissors")
    input1 = input("Player 1: ")
    input2 = input("Player 2: ")
    
    x = gamedict.get(input1.lower())
    y = gamedict.get(input2.lower())
    
    dif = x - y
    
    if dif in [-2, 1]:
        print("Player 1 is the winner")
        if(str(input("Do you want to play again?\n")) == 'yes'):
            continue
        else:
            print("Game Over")
            break
    elif dif in [2, -1]:
        print("Player 2 two is the winner")
        if(str(input("Do you want to play again?\n")) == 'yes'):
            continue
        else:
            print("Game Over")
            break
    else:
        print("It is a tie")
        if(str(input("Do you want to play again?\n")) == 'yes'):
            continue
        else:
            print("Game Over")
            break

