# Vytvořte program, který se uživatele zeptá na odvěsny A a B a přeponu C
# a vytiskne, zda je trojúhelník pravoúhlý.
# Trojúhelník je pravoúhlý právě tehdy, pokud platí C**2 == (A**2 + B**2).

oa = float(input("Zadej délku odvěsny A: "))
ob = float(input("Zadej délku odvěsny B: "))
oc = float(input("Zadej délku přepony C: "))

if oc**2 ==  (oa**2 + ob**2):
    print("Ano, jedná se o pravoúhlý trojuhelník")
else:
    print("Ne, nejedná se o pravoúhlý trojuhelník")