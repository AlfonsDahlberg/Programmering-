import math
#hela uppgift 1
num1 = int(input("skriv ett tal: "))
num2 = int(input("skriv ett till tal: "))
print("kvoten är " + str(num1 / num2))
print("det blir så här mycket över " + str(num1 % num2))
print(str(num1), "/", str(num2), "=", (math.floor(num1 / num2)), "och" ,str(num1 % num2), "1 över")
print()

# uppgift nummer 2.1 och 2.2
#1
s1 = int(input("skriv en siffra: "))
s2 = float(input("skriv ännu en siffra fast med en decimal: "))
print(float(s1))
print(int(s2))
print()
#det som händer är att eftersom man inte kan ha decimaler i en int så händer ingenting när man
#omvandlar den till en float eftersom användaren ej har skrivit in en decimal, medans i floaten
#tas decimalen användaren skrev bort.

#2.3
x = 10.5
print("x har samma värde som 10.5")
print(math.ceil(x))
print(math.floor(x))
print()
#Ceil avrundar talet upp, utan att tänka på vad decimalen är.
#Floor avrundar talet ner, utan att tänka på vad decimalen är.

#2.4
f1 = float(input("Skriv ett decimaltal: "))
f2 = int(f1)
print("ditt minsta man kan dela ditt tal i är:")
print(math.gcd(f2))
print()

#2.5
import decimal
print("omkretsen för en cirkel med radien 10 är:")
radien = 10
omkrets = (20 * math.pi)
omkrets1 = decimal.Decimal(omkrets)
print(omkrets1)
print()

#uppgift 3
#alternativ kod 1
tal1 = int(input("Skriv ett tal: "))
tal2 = int(input("Skriv ett andra tal: "))
tal3 = int(input("Skriv ett tredje tal: "))
tal4 = int(input("Skriv ett fjärde sista tal: "))
print()
print("det näst största talet är: ")
if tal1 <= tal2 and tal1 >= tal3 and tal1 >= tal4: print(tal1)
elif tal1 >= tal2 and tal1 <= tal3 and tal1 >= tal4: print(tal1)
elif tal1 >= tal2 and tal1 >= tal3 and tal1 <= tal4: print(tal1)
elif tal2 <= tal1 and tal2 >= tal3 and tal2 >= tal4: print(tal2)
elif tal2 >= tal1 and tal2 <= tal3 and tal2 >= tal4: print(tal2)
elif tal2 >= tal1 and tal2 >= tal3 and tal2 <= tal4: print(tal2)
elif tal3 <= tal1 and tal3 >= tal2 and tal3 >= tal4: print(tal3)
elif tal3 >= tal1 and tal3 <= tal2 and tal3 >= tal4: print(tal3)
elif tal3 >= tal1 and tal3 >= tal2 and tal3 <= tal4: print(tal3)
elif tal4 <= tal1 and tal4 >= tal2 and tal4 >= tal3: print(tal4)
elif tal4 >= tal1 and tal4 <= tal2 and tal4 >= tal3: print(tal4)
elif tal4 >= tal1 and tal4 >= tal2 and tal4 <= tal3: print(tal4)

#alternativ kod 2
print("det näst störst talet är: ")
integers = [tal1, tal2, tal3, tal4]
largest_integer = max(integers)
integers.remove(largest_integer)
second_largest_integer = max(integers)
print(second_largest_integer)

