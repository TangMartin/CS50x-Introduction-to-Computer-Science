text = "I am in pain"

def splitstrings(input):
    result = input.split()
    return result
    
def changeorder(input):
    x = []
    words = len(input)
    for y in range(words):
        x.append(input[words - y - 1])
    return x

def joinstrings(input):
    result = " ".join(input)
    return result
    
def reverse_v1(input):
    y = input.split()
    return " ".join(y[::-1])
    
print(joinstrings(changeorder(splitstrings(text))))
print(reverse_v1(text))