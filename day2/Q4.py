# your code goes here
rows = int(input())

for col in range(1, rows):

    for i in range(rows - col):
        print(" ", end="")

    print("*", end="")

    for i in range((col - 1) * 2 - 1):
        print(" ", end="")

    if col >= 2:
        print("*", end="")

    print("")

for i in range(rows):
    if i != rows - 1:
        print("* ", end="")
    else:
        print("*", end="")
