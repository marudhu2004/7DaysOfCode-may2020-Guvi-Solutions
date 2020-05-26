# your code goes here
rows = int(input())

for col in range(1, rows + 1):
    for i in range(col - 1):
        print(" ", end="")
    for i in range(rows - col + 1):
        if i == rows - col:
            print("*", end="")
        else:
            print("* ", end="")
    print("")
