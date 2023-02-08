
#uppgift 1
num = 2
while num <= 20:
    print(num)
    num += 2

#uppgift 2
tak = 100
summa = 0
while summa < tak:
    n = int(input("Skriv ett nummer: "))
    summa += n
    print("summa är " + str(summa))
print("Over 100")

#uppgift 3
svar = "nej"
fel = "ja"
Gissa = " "
while Gissa != svar:
    Gissa = input("Vill du spela?: ")

else:
    print("Jag vill inte spela med dig heller")

#uppgift 4
from random import *

korrektsvar = (randint(1, 100))
guess = ""
guess_count = 0
guess_limit = 10
out_of_guesses = False

while guess != korrektsvar and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = int(input("Gissa mellan ett tal 1-100: "))
        guess_count += 1
        if guess < korrektsvar:
            print("Gissa högre")
        if guess > korrektsvar:
            print("Gissa lägre")

    else:
        out_of_guesses = True



if out_of_guesses:
    print("Du gick över 10 gissningar. Försök igen.")
else:
    print("Du gissade rätt")

