import random
import string

def password(stringlength):
    str(stringlength)
    letters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(letters) for i in range (stringlength))

print(password(int(input("How many charaacters in your password: "))))