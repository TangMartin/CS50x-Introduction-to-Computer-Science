def get_int(text):
    return int(input(text))

def isprime(number):
    if(number == 1 or number == 2):
        print("This number is a composite number")
    elif(number % 2 == 0):
        print("This number is a composite number")
    else:
        print("This number is a prime number")
        
while(True):
    isprime(get_int("What is your number? "))
