#1.1
#ett och a kommer inte fungera pga av att dem inte har citat tecken annars är dom strings.
#4 är en integer.
#3.6 är en float.
#True är en boolean.
#"true" är en string.

#1.2
#variabel1 är en string
#a är en variabel för en int.
#Alpha är en boolean
#variabel2 är nada

variabel1 = 'a, b, c'
a = 10
b = 12
alpha = True
variabel2 = a
variabel3 = 1
variabel4 = b  #variabel4 är värdet b fast variabeln b har man inte anget ett värde för
#fix för detta skulle vara te. x b = 12
variablel5 = alpha #ändra variable15 till variablel5 så det matchat det vi försöker printa
print(variabel1)
print(variabel2)
print(variabel3)
print(variabel4)
print(variablel5)

#1.3
print(1/3) #det som händer i 1/3 utan citattäcken är att den tar 1/3 och printar värdet.
print('1/3') #där man har citattäcken '1/3' printar den 1/3 istället för värdet då det är än string.
a = 1/3 #en variabel för värdet av 1/3
print(a) #printar svaret av 1/3 alltså 0.3333333... osv då a är en variabel för int:en värdet av 1/3
print('a') #eftersom vi har citattäcken över a:et så printar den bara a då det är en string.

#1.4
#Error

#2.1
def beräknaArea(sida1, sida2):
    area = sida1*sida2
    return area
#funktionen beräknar arean av en rektangel genom att ta 2 argument multiplicerat med varandra
#funkar bara med ints och floats, den returnar därmed oxå bara ints och floats.
beräknaArea(2, 4)

def alternativtBeräknaArea(sida1, sida2):
    print(sida1*sida2)
    alternativtBeräknaArea(3, 15)
    #funktionen gör samma sak som den ovan bara att här har man valt att använda print i funktionen så
    #att när jag sen callar den så printas den.

def adderaSiffror(siffra1, siffra2):
    summa = siffra1+siffra2
    return summa
   # Funktionen adderar två siffror tillsammans och returnar summan av dem.
   # Funktionen tar två värden av datatypen 'int' som argument.
   # Funktionen returnerar ett värde av datatypen 'int'.

def multiplyAndAdd(x, y):
    a = x*y+y
    return a
# funktionen tar två argument, x och y, multiplicerar x och y tillsammans,
# lägger till y till resultatet och tilldelar det slutliga värdet till variabeln 'a'
#funktionen tar endast in ints och floats då multiplikation är inblandat.
#Funktionen returnerar värdet av 'a' som är av samma datatyp som argumenten x och y.
# testar funktionen med olika argument:
print(multiplyAndAdd(2, 3)) # skriver ut 8
print(multiplyAndAdd(4, 5)) # skriver ut 24
print(multiplyAndAdd(-2, 4)) # skriver ut 6

def addition(x, y):
    print(x+y)
#funktionen tar in 2 värden kan vara vad som helst både strings, ints och floats sedan så plusar dem ihop varandra.
#om det är ints eller floats så används addition men om det är 2 strings så blir det en sammansatt ord/mening
#funktionen returnar inget värde den skriver endast summan av x + y.
#testar olika argument:
addition(1, 2) #skriver ut 3
addition("Alfons"," Dahlberg ") #skriver ut "Alfons Dahlberg"


#2.3
# En funktion som tar in en lista med heltal(typen int) och returnar den sorterade listan
talLista = [1023, 757, 0, 1, 7]
def sorteraListan(talLista):
    talLista.sort() # Sorterar listan
    return talLista # returnar den sorterade listan

# Anropar funktionen med en lista av tal som argument
sorteradLista = sorteraListan(talLista)

# Skriver ut den sorterade listan
print(sorteradLista)

#3.1

#a)
#när vi adderar två tal så lägger vi ihop dem och får ett nytt tal som är summan av de två.
# Python kan göra det automatiskt för oss med "+" tecknet, så man slipper få felmeddelanden.
#Exempel:
x = 5
y = 2
z = x + y
print(z) # skriver ut 7
#Om vi istället skulle ha använt strings för x och y och inte konverterat dem till ints eller floats,
# skulle additionen överföras till en concatenation och det skulle ge oss en ny string "52"
# istället för inten 7.
#exempel:
x = "5"
y = "2"
z = x + y
print(z) # utskrift: "52"
#b)
#funktionen frågar användaren om deras favorit tal mellan 1-15 inkulsive floats/decimaler.
#den ger sedan ett svar baserat på vad användaren valde.
def favoritTal():
    while True:
        # Be användaren om deras favorit tal
        favoritTal = float(input("Vilket är ditt favorit tal mellan 1-15 (inklusive decimaltal)? "))
        # Kolla om talet är ett giltigt val (mellan 1 och 15)
        if favoritTal >= 1 and favoritTal <= 15:
            # Kolla om talet är 1-6 eller 7-15
            if favoritTal <= 6:
                print("Jag håller med dig ! :)")
            else:
                print("Jag håller inte med dig :(.")
            break
        else:
            print("Vänligen välj ett tal mellan 1 och 15.")
favoritTal()

#3.2
# använderan skriver ett tal
num1 = float(input("Ange det första talet: "))

# användaren väljer vilken operation hen vill använda
operation = input("Välj operation (+, -, *, /, %, //, ^, sqrt): ")

# användaren skriver in ett till tal om det behövs för operationen (behövs inte för sqrt)
if operation != "sqrt":
    num2 = float(input("Ange det andra talet: "))

# Programmet använder operationen man valde för dem 2  talen
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 == 0:
        print("Kan inte dela på 0!") #fixar så att när man delar med 0 så crashar inte programmet
    else:
        print(num1 / num2)
elif operation == "%":
    if num2 == 0:
        print("Kan inte dela på 0!") #fixar så att när man delar med 0 så crashar inte programmet
    else:
        print(num1 % num2)
elif operation == "//":
    if num2 == 0:
        print("Kan inte dela på 0!") #fixar så att när man delar med 0 så crashar inte programmet
    else:
        print(num1 // num2)
elif operation == "^":
    print(num1 ** num2)
elif operation == "sqrt":
    print(num1 ** 0.5)
else:
    print("Ogiltig operation") #ifall användaren inte skriver någon av dem angivna operationerna
    # så kommer programmet inte crasha

#3.4
def kontrolleraInput(inputS):
    # Kontrollera om längden på input är mer än 8 tecken
    if len(inputS) > 8:
        return False
    # Kontrollera om input innehåller "å, ä, ö"
    if 'å' in inputS or 'ä' in inputS or 'ö' in inputS:
        return False
    return True


anvandarInput = input("skriv något: ")

# printar ut ett svar beroende på inputen
if kontrolleraInput(anvandarInput):
    print("godkänt")
else:
    print("inte godkänt")
#4.1
q = input("skriv något: ")
antalBokstäver = 0
antalSiffror = 0
for c in q: #en loop för varje tecken ints, floats, strings etc i q.
    if c.isdigit(): #kollar antalet siffror
        antalSiffror = antalSiffror + 1 #lägger till en varje gång den hittar en
    elif c.isalpha(): #kollar antalet bokstäver
        antalBokstäver = antalBokstäver + 1 #lägger till en varje gång den hittar en
print("antal bokstäver =" + str(antalBokstäver))
print("antal siffror =" + str(antalSiffror))
#4.2
#olika startvärden
f1 = 0
f2 = 1
f3 = 1
svar = "0, 1"
while f3 < 50: #medans nästa tal eller mindre än 50 fortsätts loopen
    svar = svar + ", " + str(f3)
    f3 = f1 + f2 #räkna ut nästa tal
    f1 = f2 # förbred för nästa uträkning
    f2 = f3 # samma sak som ovan
print(svar)

#5
#Clash of Clans
#1) en gång varje timme då jag har blivit anfallen i spelet.
#2)30 minuter per dag
#3)Ja man kan köpa för att få uppgraderingar.

#7
elever = ['Axel', 'Johan', 'Johanna', 'Oscar', 'Bill']
nummer = [1, 3, 4, 6, 2, 5]

elever.sort()
nummer.sort()

for x in elever: print (x)
for x in nummer: print (x)


elever.append("a")
elever.append("b")
print(elever)
print(elever.sort())

for x in elever:
    if x == "":
        print("det finns minst 1 tom elemt")
        break   #för siffrorna samma sak men andra variabler.

elever2 = elever.copy