# your code goes here
s = input()

if (
    s.isupper()
    and len(s) == 10
    and s[:5].isalpha()
    and s[5:-2].isnumeric()
    and s[-1].isalpha()
):
    print("pan")
else:
    print("not pan")
