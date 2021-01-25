import random

rnd = [True, False]
masss = [[[random.choice(rnd) for i in range(1, 22)] for j in range(1, 16)] for z in range(1, 5)]
for z in range(len(masss)):
    print(z, "Поверх")
    for y in range(len(masss[z])):
        for x in range(len(masss[z][y])):
            print(x, masss[z][y][x], end=" ")
        print()

