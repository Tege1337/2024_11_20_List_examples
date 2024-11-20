"""
Hozz létre két listát: [3, 1, 4] és [9, 7, 2]. 
Egyesítsd a két listát, és rendezd a lista elemeit növekvő sorrendbe!
"""


# írasd ki az első és az utolsó elemet!

list_1 = [3, 1, 4]
list_2 = [9, 7, 2]

list_3 = [x for y in (list_1, list_2) for x in y]
print(sorted(list_3))