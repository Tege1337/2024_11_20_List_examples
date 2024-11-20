"""
Hozz létre egy listát számokkal: [5, 8, 12, 15, 22].
Határozd meg a lista hosszát egy ciklus segítségével 
(a len() függvény megoldásán kívül használj for ciklusos megoldást is),
és írd ki!
"""

nums = [5, 8, 12, 15, 22]

nums_num = 0
for x in nums:
    nums_num += 1

print(nums_num) # with the for cycle
print(len(nums)) # without the for cycle