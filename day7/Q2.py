size = int(input())
input_list = [int(i) for i in input().split(" ")]

for j in range(size):
    for i in range(size - 1):
        if input_list[i] > input_list[i + 1]:
            input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
    for i in input_list[:-1]:
        print(i, end=" ")
    print(input_list[-1])
    print("")
