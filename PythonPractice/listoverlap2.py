import random

a = random.sample(range(20), 10)
b = random.sample(range(20), 10)
result = [x for x in a if x in b]

print(a)
print(b)
print(result)