import array

def display_grid(VankinsGrid):
    for r in range(len(VankinsGrid)):
        for c in range(len(VankinsGrid[0])):
            print(str(VankinsGrid[r][c]), end = "\t")
        print("")

def evalunit(VankinsGrid, r = 0, c = 0):
    unitscore = VankinsGrid[r][c]
    upscore = 0
    leftscore = 0
    if(r < len(VankinsGrid) - 1):
        upscore = evalunit(VankinsGrid, r + 1, c)
    if(c < len(VankinsGrid[0]) - 1):
        leftscore = evalunit(VankinsGrid, r, c + 1)
    return max(upscore + unitscore, leftscore + unitscore)

randGr =      [ [1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 0], 
                [2, 1, 2, 3, 5], 
                [5, 5, 1, 9, 5], 
                [0, 9, 9, 9, 7] ]

TestGr1 =     [ [5 ,-2], 
                [-3, 1] ]

TestGr2 =     [ [1, 2, 3],
                [2, -10, -20],
                [-20, 20, 10] ]

TestGr3 =     [ [8, -6, 0], 
                [-6, -6, 7], 
                [7, -3, -3], 
                [-6, 4, -9] ]

print("Welcome to Vankins Mile")
display_grid(TestGr2)
score = evalunit(TestGr2)
print("The maximum score possible on this grid is " + str(score))
