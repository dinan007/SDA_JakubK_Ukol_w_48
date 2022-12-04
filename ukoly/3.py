# Vytvořte program, který se uživatele zeptá na dvě celá kladná čísla (int) A a B
# a vypíše, zda se rovnají nebo které z nich je větší a menší.

cislo_jedna = int(input("Zadej celé kladné číslo A:\n"))
cislo_dva = int(input("Zadej celé kladné číslo B:\n"))

if cislo_jedna == cislo_dva:
    print("Číslo A i B jsou stejné.")
elif cislo_jedna > cislo_dva:
    print("Číslo A je vetší než číslo B.")
elif cislo_jedna < cislo_dva:
    print("Číslo A je menší než číslo B.")