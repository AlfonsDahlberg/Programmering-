l = int(input("skriv en siffra: "))
while l>=-1:  
    l=l+1
    j = str(input("Skriv ja om du vill fortsätta: "))
    o = "ja"
    if j==o:
        print(l) #användaren skriver "ja" och loopen fortsätts.
    else:
        break  #Ifall användaren inte skriver ja, att dem vill fortsätta kommer break att användas.
               #Det betyder att loopen avbryts och går vidare till nästa bit av koden.
print("end")








