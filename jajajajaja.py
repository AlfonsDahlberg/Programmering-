#Alfons Dahlberg
#uppgift 1
ord1 = str(input("Skriv ett ord: "))

print("Ordet har " + str(len(ord1)) + " bokstäver")
if len(ord1) <=2:
    print ("Ordet innehåller inte 3 bokstäver")
else :print(ord1[0], ord1[1], ord1[2])
if ord1.find("a") != -1:
    print("Index av första a som kommer upp är " + str(ord1.find("a")))
else :print("Det finns inget a i detta ord")
if ord1.islower():
    print("Alla bokstäver är små")
else :print("Alla bokstäver är inte små")








