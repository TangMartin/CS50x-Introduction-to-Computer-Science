def main():
    divisors = []
    number = int(input("Number: "))
    numberstodivide = range(1, (number + 1))
    
    for i in numberstodivide:

        if(number % i == 0):
            divisors.append(i)
        else:
            continue
        
    print(divisors)
        
main()