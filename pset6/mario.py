from cs50 import get_int

height = -1
while height < 1 or height > 8:
    height = get_int("Height: ")
 
x = height 
for i in range(height + 1):
    if i > 0:
        for k in range(x - 1):
            print(" ", end="")
        x -= 1
    for j in range(i):
        print("#", end="")
    if i > 0:
        print()
    
        
        