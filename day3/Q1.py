# your code goes here
s = input()

has_consonents = False
pro_s = ""

for i in s:
    if not (i in "AEIOUaeiou"):
        pro_s += i
        if i.isalpha():
            has_consonents = True

if has_consonents:
    print(pro_s)
else:
    print(-1)
