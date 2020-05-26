# your code goes here
list_len = int(input())
nodes = input("").split(" ")
roll = int(input())
rotated = []

if list_len > 0:
    for i in range(list_len):
        rotated.append(nodes[(i + roll) % list_len])
    for i in rotated:
        print(i, end=" ")
else:
    print()
