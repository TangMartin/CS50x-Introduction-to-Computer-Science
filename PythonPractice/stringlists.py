def main():
    word = input("Word: ")
    letters = len(word)
    counter = 0

    for x in range(round(letters / 2)):
        if(word[x] == word[letters - 1 - x]):
            counter += 1
        else:
            continue
    
    if(round(letters / 2) == counter):
        print("The word is a palindrome")
    else:
        print("The word is not a palindrome")
        

wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
    

