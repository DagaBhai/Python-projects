import random

def gridgen():
    matrix = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        total_number = list(range(1, 10))
        random.shuffle(total_number)
        for j in range(9):
            valid = False
            attempts = 0
            while not valid and attempts < 50:
                num = total_number.pop()
                if num not in [matrix[x][j] for x in range(i)]:
                    matrix[i][j] = num
                    valid = True
                else:
                    total_number.insert(0, num)
                attempts += 1

    return matrix

grid = gridgen()

for i in grid:
    print(i)