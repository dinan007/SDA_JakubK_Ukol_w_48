# Vytvořte program, který se uživatele zeptá na jméno,
# věk a hobby. Poté vytiskněte na obrazovku v nějáké smysluplné zprávě
# jeho jméno, věk, hobby a kolik let mu bude příští rok.

jmeno = input ("Zadejte své jméno: ")
vek = int(input("Zadejte svůj věk: "))
hobby = input("Jaké je tvé hobby: ")

vek_bude = (vek + 1)

print(f"Zjistil jsem, že se jmenuješ {jmeno}. Momentálně je ti {vek} roků a tvým největším koníčkem je {hobby}.")
print(f"Jo a je celkem jasný, že od dalších narozenin bude to číslo horší. Už to bude {vek_bude} :):):)")