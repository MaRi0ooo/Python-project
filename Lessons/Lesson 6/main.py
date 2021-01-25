board1 = [[i for i in range(1, 9)] for j in range(1, 9)]
for x in range(len(board1)):
    for y in range(len(board1[x])):
        if (y % 2 == 0 and x % 2 == 0) or (y % 2 == 1 and x % 2 == 1):
            board1[x][y] = "▒"
        else:
            board1[x][y] = "█"
        print(board1[x][y], end=" ")
    print()

print(2, "wariant")

for x in range(len(board1)):
    for y in range(len(board1)):
        if (y % 2 == 0 and x % 2 == 0) or (y % 2 == 1 and x % 2 == 1):
            board1[y][x] = "▒"
            board1[0][0] = "Л"
            board1[0][1] = "к"
            board1[0][2] = "С"
            board1[0][3] = "Ф"
            board1[0][4] = "К"
            board1[0][5] = "С"
            board1[0][6] = "к"
            board1[0][7] = "Л"
            board1[1][0] = "п"
            board1[1][1] = "п"
            board1[1][2] = "п"
            board1[1][3] = "п"
            board1[1][4] = "п"
            board1[1][5] = "п"
            board1[1][6] = "п"
            board1[1][7] = "п"
            board1[7][0] = "Л"
            board1[7][7] = "Л"
            board1[7][1] = "к"
            board1[7][6] = "к"
            board1[7][5] = "С"
            board1[7][4] = "K"
            board1[7][3] = "Ф"
            board1[7][2] = "C"
            board1[6][0] = "п"
            board1[6][1] = "п"
            board1[6][2] = "п"
            board1[6][3] = "п"
            board1[6][4] = "п"
            board1[6][5] = "п"
            board1[6][6] = "п"
            board1[6][7] = "п"
        else:
            board1[y][x] = "█"

        print(board1[x][y], end=" ")
    print()
