a = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]

def setremove(lists):
    return set(lists)
    
def loopremove(lists):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    return b

print(a)
print(setremove(a))
print(loopremove(a))