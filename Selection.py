import math
sudokuGrid = [
    [7,0,0,0,3,4,8,0,0],
    [8,0,4,6,0,0,0,0,0],
    [0,3,9,0,5,0,0,0,0],
    [1,0,0,5,0,0,6,0,0],
    [0,4,0,7,0,9,0,3,0],
    [0,0,3,0,0,8,0,0,9],
    [0,0,0,0,7,0,3,2,0],
    [0,2,6,0,0,1,9,0,5],
    [0,0,7,9,2,0,0,0,4]
]
size = len(sudokuGrid)
print("Sudoku grid size is ", size, " by ", size)
for row in range(size):
    print(sudokuGrid[row])
area = int(math.sqrt(size))
print("Size of each area is: ", area, " by ", area)
gridUpdated = True
while gridUpdated:
    gridUpdated = False
    for target in range(1, size+1):
        row = 0
        while row < size:
            col = 0
            while col < size:
                print("\nChecking the following area for target value: ", target)
                print("start row: ", row)
                print("end row: ", row + area - 1)
                print("start col: ", col)
                print("end col: ", col + area - 1)
                print()
                foundTarget = False
                for r in range(row, row + area):
                    for c in range(col, col + area):
                        if sudokuGrid[r][c] == target:
                            foundTarget = True
                            break
                print("The target value ", target, end=" ")
                if not foundTarget:
                    print(" was not in area")
                    placeTargetAT = []
                    for r in range(row, row+area):
                        for c in range(col, col+area):
                            print("Checking row ", r, " column ", c)
                            if sudokuGrid[r][c] == 0:
                                print("Square available")
                                currentRowValues = sudokuGrid[r]
                                currentColValues = [item[c] for item in sudokuGrid]
                                if target not in currentRowValues and target not in currentColValues:
                                    print("Could place ", target, " at (", r, ",", c, ")")
                                    placeTargetAT.append([r, c])
                                print("Row contains ", currentRowValues)
                                print("Col contains ", currentColValues)
                    if len(placeTargetAT) == 1:
                        print("Placed ", target, " at ", placeTargetAT[0][0], " x ", placeTargetAT[0][1])
                        sudokuGrid[placeTargetAT[0][0]][placeTargetAT[0][1]] = target
                    gridUpdated = True
                else:
                    print("was found in area")
                col += area
            row += area
    for row in range(0, size):
        if 0 in sudokuGrid[row]:
            for col in range(0, size):
                if sudokuGrid[row][col] == 0:
                    currentRowValues = sudokuGrid[row]
                    currentColValues = [item[col] for item in sudokuGrid]
                    validChoices = []
                    for n in range(1, size+1):
                        if n not in currentRowValues and n not in currentColValues:
                            validChoices.append([row, col, n])
                    if len(validChoices) == 1:
                        x = validChoices[0][0]
                        y = validChoices[0][1]
                        n = validChoices[0][2]
                        sudokuGrid[x][y] = n
                        gridUpdated = True


for row in range(size):
    print(sudokuGrid[row])

