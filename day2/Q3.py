# your code goes here
rows = int(input())

for col in range(1, rows + 1):
    for i in range(rows - col):
        print(" ", end="")

    for i in range(col):
        print("*", end="")

    print("")
