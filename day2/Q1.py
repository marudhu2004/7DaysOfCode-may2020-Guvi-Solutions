# your code goes here
num = input().split(" ")

# Getting the row and column values
row = int(num[0])
col = int(num[1])

if not (1 <= row <= 100 and 1 <= col <= 100):
    print("Invalid input")
    quit()

for i in range(row):
    if i == 0 or i == row - 1:
        for j in range(col):
            if j == col - 1:
                print("*", end="")
            else:
                print("* ", end="")

    else:
        for j in range(col):
            if j == 0:
                print("*", end="")
            elif j == col - 1:
                print(" *", end="")
            else:
                print("  ", end="")

    print("")
