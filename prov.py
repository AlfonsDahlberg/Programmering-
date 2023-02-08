n1 = float(input("Skriv ett tal: "))
n2 = float(input("Skriv ett till tal: "))
n3 = float(input("Skriv ett sista tal: "))

list1 = [n1, n2, n3]
print(list1)

def sortering():
    if n1 < n2 and n1 < n3 and n2 < n3:
        print([n1, n2, n3])
    if n2 < n1 and n2 < n3 and n1 < n3:
        print([n2, n1, n3])
    if n3 < n1 and n3 < n2 and n1 < n2:     #lyckades ej, men jag ville att alla kombinationer skulle kunna sortera.
        print([n3, n1, n2])

list1.sort()
print(list1)      #den här strategien är utan if satsen och funktion men den funkar genom att den  sorterar.



