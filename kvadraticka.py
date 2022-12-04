import math

a = input("Zadej A: ")
b = input("Zadej B: ")
c = input("Zadej C: ")

if not a.isdigit() or not b.isdigit() or not c.isdigit():
#      a                  2                  3
#      False              True               True
#~     True               False              False
#|     True                        False
#|                    True
    print("Nevalidní vstup!")
    exit()

# Výpis
print(f"{a}x^2 + {b}x + {c} = 0")

# Přetypování str na int
a = int(a)
b = int(b)
c = int(c)

# Determinant
det = b**2 - (4*a*c)

# 2 kořeny
if det > 0:
    x1 = ( -b + math.sqrt(det) ) / 2 * a
    x2 = ( -b - math.sqrt(det) ) / 2 * a

    print(f"X1: {x1} X2: {x2}")
# 1 kořen
elif det == 0:
    x = -b / 2 * a
    print(f"X: {x}")
else:
    print("Nemá řešení v R")