s = input()
brackets = r"{[()]}"
found_brackets = []
had_proper_brackets = False
bracket_relation = {"{": "}", "[": "]", "(": ")"}

for i in s:
    if i in brackets:
        had_proper_brackets = True
        found_brackets.append(i)
i = 0

while found_brackets:
    try:
        cur_bracket = ""
        if found_brackets[i] in brackets[3:]:
            cur_bracket = found_brackets[i - 1]
            if found_brackets[i] == bracket_relation[cur_bracket]:
                found_brackets.pop(i - 1)
                found_brackets.pop(i - 1)
                i = 0
        i += 1
    except Exception:
        had_proper_brackets = False
        break

if (not found_brackets) and had_proper_brackets:
    print("yes")
else:
    print("no")
