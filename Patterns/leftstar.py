rows = int(input("Enter number of rows="))
i = 1
while i <= rows:
    j = i
    while j < rows:
        # printing spaces before stars
        print(' ', end=' ')
        j += 1
    k = 1
    # print stars
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1
# for downside output of star pattern
i = rows
while i >= 1:
    j = i
    while j <= rows:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1