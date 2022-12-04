# Získá vstup od uživatele
vstup = input("Ahoj jsem papušek Lojza. Něco mi řekni:\n")
# vypsání vstupu
# print(type(vstup))

# Formátování stringů - old school
print("Uživatel zadal: %s %s" % (vstup, 1))
# Formátování stringů - novější
print("Uživatel zadal novější: {uzi_vstup}".format(uzi_vstup=vstup))
# Formátování stringů - nějnovější
print(f"Uživatel zadal nejnovější: {vstup}")