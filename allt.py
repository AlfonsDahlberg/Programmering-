import random
from random import sample
print("hej")
for i in range(10):
    print(random.randint(0, 20))

print("hej")
for i in range(10):
    print(random.gauss(0, 20))

print("hej")
list1 = [1, 2, 3, 4, 5]
print(sample(list1, 3))




name = input("name: ")
age = int(input("age: "))
try:
    print(name + age)
    print(1)
except TypeError:
    print(name + str(age))
    print(2)

#ingen except slutar på 0
#for i in range(-10, 5):
    #print(1/i)

#med exceot
for i in range(-10, 5):
    try:
        print(1/i)
    except:
        print(i/(i+1))





