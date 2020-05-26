import math

args = input().split(" ")
N, Q = int(args[0]), int(args[1])
L = input().split(" ")

out = 0

for i in L:
    num = int(i)
    while num > 0:
        num -= math.ceil(num / 2)
        out += 1

print(out)
