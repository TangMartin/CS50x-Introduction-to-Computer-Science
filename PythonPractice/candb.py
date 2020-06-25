import random
import sys

def get_int():
    inputs = input("What is the 4 digit number: ")
    if(inputs == "exit"):
        sys.exit()
    return int(inputs)

def coworbull(numberlist, guesslist):
    global win
    cow = 0
    bull = 0
    done = False
    
    for x in range(len(numberlist)):
        for x in range(len(numberlist)):
            if(numberlist[x] == guesslist[x]):
                cow += 1
                numberlist.remove(numberlist[x])
                guesslist.remove(guesslist[x])
                break
            else:
                continue
            
    
    for x in range(4):
        for x in range(len(numberlist)):
            for y in range(len(numberlist)):
                if(numberlist[x] == guesslist[y]):
                    bull += 1
                    numberlist.remove(numberlist[x])
                    guesslist.remove(guesslist[y])
                    done = True
                    break
                else:
                    continue
            if done:
                break
            
    print("There is/are", cow, "cows and", bull, "bulls")
    if(cow == 4):
        win = True
    else:
        win = False
        
if __name__=="__main__":
    
    randomnumber = random.randint(1000, 9999)
    win = False
    counter = 0
    
    while(win == False):
        guess = list(str(get_int()))
        number = list(str(randomnumber))
        coworbull(number, guess)
        counter += 1
    
    print("Congratulations, it took you", counter, "tries")
    
    
    
        
    
        
        
        
    
    
    
    
    
