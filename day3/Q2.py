# your code goes here
s = input()


def rem_dupli(s):

    fwd = ""
    prev = ""
    final_str = ""
    duplicates = False
    for i in range(len(s)):
        try:
            fwd = s[i + 1]
        except IndexError:
            fwd = ""
        if not (s[i] == prev or s[i] == fwd):
            final_str += s[i]
        else:
            duplicates = True
        prev = s[i]
    return final_str, duplicates


while True:
    s, duplicates = rem_dupli(s)
    if not duplicates:
        break

print(s)
