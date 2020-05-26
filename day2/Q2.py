# your code goes here
rows = int(input())

num = 1
for col in range(rows + 1):
    for i in range(col):
        if i == col - 1:
            print(num, end="")
        else:
            print(str(num) + " ", end="")
        num += 1
    print("")
