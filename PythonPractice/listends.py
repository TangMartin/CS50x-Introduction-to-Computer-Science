import random

a = random.sample(range(100), 5)
results = []

results.append(a[0])
results.append(a[len(a) - 1])

print(a)
print(results)