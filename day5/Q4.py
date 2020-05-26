# your code goes here
s1 = input()
s2 = input()
s_len = len(s2)
flag = False
roll = 0
for i in range(s_len):
    inter = ""
    for j in range(s_len):
        inter += s2[(j + roll) % s_len]
    roll += 1
    if s1 == inter:
        flag = True
        break

if flag:
    print("1")
else:
    print("0")
