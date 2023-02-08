#Import math Library
import math

täljare1 = int(input("Skriv en täljare: "))
print("/")
nämnare1 = int(input("Skriv en nämnare: "))
print("/")
täljare2 = int(input("Skriv en till täljare: "))
print("/")
nämnare2 = int(input("Skriv en till nämnare: "))
print("/")
täljare3 = int(input("Skriv en sista täljare: "))
print("/")
nämnare3 = int(input("Skriv en sista nämnare"))

bråk1 = int(täljare1) / int(nämnare1)
bråk2 = int(täljare2) / int(nämnare2)
bråk3 = int(täljare3) / int(nämnare3)

GN = nämnare1 * nämnare2 * nämnare3
GT1 = täljare1 * nämnare2 * nämnare3
GT2 = täljare2 * nämnare1 * nämnare3
GT3 = täljare3 * nämnare1 * nämnare2
print(GT1 + GT2 + GT3)
print("/")
print(GN)
print()
x = math.gcd (GT1 + GT2 + GT3, GN)
if x != 0:
    print ((GT1 + GT2 +GT3)/x)
    print("/")
    print(GN / x)
else:
    print(GT1 + GT2 + GT3)
    print("/")
    print(GN)




