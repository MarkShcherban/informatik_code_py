summe = 0

while True:
    zahl = int(input("Geben Sie bitte eine Zahl ein: "))

    if zahl == 0:
        break
    
    elif zahl < 0:
        continue

    else:
        summe += zahl

print(f"Die Summe ist {summe}")
