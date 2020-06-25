def main():
    list = []
    listten = []
    for i in range(5):
        x = int(input("Number: "))
        list.append(x)
    for element in list:
        if(element < 10):
            listten.append(element)
        else:
            continue
    print("Numbers that are less than 10: ")
    for x in listten:
        print(x)

main()