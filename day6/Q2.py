s = input()
found_brackets = []
proper_brackets_count = 0

for i in s:
    if i in "()":
        found_brackets.append(i)
i = 0

while found_brackets:
    try:
        if found_brackets[i] == ")" and found_brackets[i - 1] == "(":
            found_brackets.pop(i - 1)
            found_brackets.pop(i - 1)
            proper_brackets_count += 1
            i = 0
        i += 1
    except Exception:
        break

if proper_brackets_count:
    print(proper_brackets_count * 2)
else:
    print(-1)
