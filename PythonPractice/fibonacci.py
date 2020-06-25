def fibonnaci(number):
    lists = [1, 1]
    if(number == 1):
        lists = [1]
        return lists
    elif(number == 0):
        lists = []
        return lists
    for x in range(number - 2):
        lists.append(lists[x] + lists [x + 1])
    return lists

print(fibonnaci(int(input("Number of Fibonnaci: "))))