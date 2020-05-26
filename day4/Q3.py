# your code goes here
list_len = int(input())
number = input().split(" ")
carry = 0

if list_len > 0:
    number[-1] = int(number[-1]) + 1

    for i in range(list_len - 1, -1, -1):

        number[i] = int(number[i]) + carry

        if int(number[i]) > 9:
            number[i] = int(number[i]) - 10
            carry = 1
        else:
            carry = 0

    if carry:
        number.insert(0, carry)

    for i in number[:-1]:
        print(i, end=" ")

    print(number[-1])

else:
    print()
