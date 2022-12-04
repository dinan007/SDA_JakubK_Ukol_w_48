# Získat vstup od uživatele (2 celá čísla neboli int)
a = input("Zadej dělenec: ")
b = input("Zadej dělitel: ")

# Ošetřti vstup a převést na int
if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    if b == 0:
        print("Dělitel nesmí být 0")
        #exit()
    else:
        c = a / b

        print(f"Podíl je {c}")
        print(f"Podíl je {a/b}")
# Pokud není vstup celé čislo (.isdigit()) tak vypsat hlášku
else:
    print("Tohle není validní vstup!")

# Pokud je vstup OK vypsat podíl