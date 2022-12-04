# Vytvořte program pro náhodný hod kostkou.
# Uživatel zadá interval/rozsah ve kterém se mají náhodná čísla generovat.
# Použijte funkci randint z modulu random. Vstupem funkce randint je rozsah jako dvě celá čísla (int).
# Například:
# a = 1
# b = 10
# random.randint(a, b) -> náhodné číslo mezi 1 až 10 (včetně)

import random

a = int(input("Jsem tvá kostka. Zvol si rozsah čísel své kostky a já hodím tvou kostkou a sdělím ti číslo.\nZadej počáteční číslo rozsahu kostky: "))
b = int(input("Zadej konečné číslo rozsahu tvé kostky: "))

n_cislo = random.randint(a, b)

print(f"Hod koskou ukázal číslo: {n_cislo}")
