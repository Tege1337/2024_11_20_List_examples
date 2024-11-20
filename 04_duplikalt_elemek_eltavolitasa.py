"""
Hozz létre egy listát számokkal, ahol előfordulhatnak duplikációk: [1, 2, 2, 3, 3, 4, 5, 5].
Távolítsd el a duplikált számokat, és írd ki az eredményt!
"""

# set-es megoldás

numbers_list = [1, 2, 2, 3, 3, 4, 5, 5]
numbers_set = set(numbers_list)

print(numbers_set)