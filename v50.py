#öppnar en beffintlig fil och printar innehållet.
file = open("hejehj.txt", "r")
print(file.read())
file.close()
#skappar en fil och skriver in text för att sedan stänga den.
path = ("C:\\User\\AlfonsDahlberg\\Desktop\\hejhej22.txt")
file=open(path, "w+")
file.write("hejhejhej")
file.close()

list = [1,2,3,4,5]
x = 2
for i in range(x):
    r = random.randint(1,5) #  random input mellan 1 och 5.
    print(list[r-1]) #  index 5 inte finns i listan måste jag ta -1.
    r = random.randint(1, 5)
    print(list[r-1])
print("\n")
