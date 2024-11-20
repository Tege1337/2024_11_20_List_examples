# gyümölcsök kiíratása
gyumolcsok = ['alma', 'körte', 'szilva', 'barack']

for x in gyumolcsok:
    print(x)

print()

# hónapok kiíratása
honapok = ['január', 'február','március', 'április', 'május', 'június', 'július'] 

for x in honapok:
    print(x)

print()

# index megjelenítése:
    # 0 január
    # 1 február

index = 1
for x in honapok:
    print(f"{index} - {x}")
    index += 1

print()

# index felhasználása sorszámok megadásához:
    # 1. január
    # 2. február

index = 1
for x in honapok:
    print(f"{index}. {x}")
    index += 1