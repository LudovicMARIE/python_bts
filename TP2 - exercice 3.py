import random

count = 0
i = 0

for i in range(0,10):
    nombre = random.randrange(1,10)
    count = count + nombre
    i = i+1
count = count/i
print(count)

