# Vytvořte program, který se uživatele zeptá na celé kladné číslo (int)
# a vytiskne na obrazovku, zda je liché nebo sudé.
# Pomůže vám k tomu operátor % (modulo).

cislo = int(input("Zadejte celé kladné číslo:\n"))

if cislo % 2 == 0:
    print("Bylo zadáno sudé číslo.")
else:
    print("Bylo zadáno liché číslo.")