n = 16
print("*" * n, end="\n")
i = (n//2) - 1
j = 2

while i != 0:
    while j <= (n-2):
        print("*" * i , end= "")

        print(" " * j, end="")
        print("*" * i)
        i = i - 1
        j = j + 2
