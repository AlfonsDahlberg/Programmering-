#uppgift 1
ord1 =  input("Skriv ett ord: ")

for letter in ord1:
    print("(" + letter + ")")

#uppgift 2
N = int(input("välj ett tal: "))
L = " "
for a in range(0, N):
    print("|" + str(a * L) + "\\")
    a = a + 1

#uppgift 3
n = int(input("Skriv ett nummer: "))
B = "-"
m = " "
sida = "|"
print(m + 2*n*B)
for c in range(0, n):
    print(sida + 2*n*m + sida)
print(m + 2*n*B)



#uppgift 4
x = int(input("välj en siffra: "))
z = 0
for a in range(x):
    a+= 1
    z+= a

print(" =", (z))

#uppgift 5
#(jag använde h och g istället för n och m pga att jag använde dem i tidigare uppgifter)
h = int(input("Skriv in ett tal: "))
g = int(input("Skriv in ett till tal: "))
sum = 0
if h <= g:
    number1 = range(h, g)
    for T in number1:
        sum += T
    print(sum)


2