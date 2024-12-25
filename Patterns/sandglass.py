rows = int(input("Enter rows: "))

for i in range(1, rows):
    for j in range(1,i):
        print('', end= ' ')

    k=i
    for k in range(i, rows+1):
        print('*', end=' ')

    print()

    i = rows - 1
    while i >= 0:
        j = 0
        while j < i:
            print('', end=' ')
            j += 1
        k = i 
        while k <= rows - 1:
            print('*', end=' ')
            k += 1
        print('')
        i -= 1

