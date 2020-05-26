# your code goes here
s = input().split(" ")
duplicates = True


def format(s):
    final_str = []
    current_word = ""
    duplicates = False
    while s:
        try:
            current_word = s[0]
            s.pop(0)
            if current_word != s[0]:
                final_str.append(current_word)
            else:
                duplicates = True
                s.pop(0)
        except IndexError:
            final_str.append(current_word)
    return final_str, duplicates


while duplicates:
    s, duplicates = format(s)

if s != [] or s == [""]:
    for i in s:
        print(i, end=" ")
else:
    print(-1)
