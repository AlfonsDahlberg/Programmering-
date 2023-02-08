def sayhi(name):
   print("hello " + name)

name = str(input("Vad heter du: "))

sayhi(name)

def cube(num):
    return num*num*num

num = int(input("Skriv ett nummer: "))

print("Ditt nummer ^3 blir " + str(cube(num)))
