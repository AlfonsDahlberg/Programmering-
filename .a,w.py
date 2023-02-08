a = str(input("Skriv någonting: "))
if len(a) > 7:
    print("Det du vlade att skriva är för långt!")
FörbjudnaTecken1 = "å"
FörbjudnaTecken2 = "ä"
FörbjudnaTecken3 = "ö"
if FörbjudnaTecken1 or FörbjudnaTecken2 or FörbjudnaTecken3 in a:
    print("Du valde att använda dig av förbjudna tecken!")


