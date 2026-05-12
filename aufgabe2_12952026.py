betrag = 50

while betrag > 0:
    preis = int(input("Wie viel kostet diese Ware?: "))

    if preis == 0:
        break
    elif preis < 0:
        print("Ungueltiger Preis!")
        continue
    elif betrag - preis < 0:
        print(f"Das ist zu teuer! Sie haben nur {betrag} Euro!")
        continue
    else:
        betrag -= preis

print(f"Restbetrag ist {betrag} Euro") 