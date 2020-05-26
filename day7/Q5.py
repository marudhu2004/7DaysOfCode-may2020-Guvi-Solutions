in_str = input()
cap_mask = []
upper = []
lower = []

for i in in_str:
    if i.isupper():
        cap_mask.append(1)
        upper.append(i)
    else:
        cap_mask.append(0)
        lower.append(i)

upper.sort()
lower.sort()

for i in range(len(in_str)):
    if cap_mask[i]:
        print(upper[0], end="")
        upper.pop(0)
    else:
        print(lower[0], end="")
        lower.pop(0)
