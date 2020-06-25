number = -1
while(number <= 0):
    number = int(input("Number: "))
if(number % 2 == 0 and number % 4 != 0):
    print("Number is Even")
elif(number % 2 == 0 and number % 4 == 0):
    print("Number is a multiple of four")
else:
    print("Number is Odd")
    
    