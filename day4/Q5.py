# your code goes here
list_len = int(input())
number = input().split(" ")
chunk = int(input())
intermediate = []
final = []

for i in range(0, list_len + 1, chunk):
    items = []
    for j in range(chunk):
        try:
            items.append(number[i + j])
        except Exception:
            break
    if items:
        intermediate.append(items)

for i, j in enumerate(intermediate):
    if not i % 2:
        j.reverse()

for item in intermediate:
    for i in item:
        final.append(i)

for i in final[:-1]:
    print(i, end=" ")

print(final[-1])
