rows = int(input("Enter Rows: "))
space = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(space, 0, -1):
        print(end=" ")
    space += 1
    
    for j in range(0, i+1):
        print("*",end= ' ')
    print("")