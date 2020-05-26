# your code goes here
s = input()

words = s.split(" ")
final = ""

for index, word in enumerate(words):
    if index == 0:
        final += word + " "
    elif index == len(words) - 1:
        final += word
    else:
        final += word[::-1] + " "

print(final)
