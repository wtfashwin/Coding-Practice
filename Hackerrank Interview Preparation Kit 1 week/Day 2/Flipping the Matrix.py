'''
Sean invented a game involving a matrix where each cell of the matrix contains an integer. He
can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum


'''

q = int(input())
for _ in range(q):
    
    n = int(input())
    a = []
    
    for y in range(2*n):
        a.append([int(x) for x in input().split()])
    sumofa = 0
    
    for i in range(n):
        for j in range(n):
            sumofa += max(max(a[i][j],a[2*n-i-1][j]),max(a[i][2*n-j-1],a[2*n-i1][2*n-j-1]))
    
    print(sumofa)
