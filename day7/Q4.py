list_len = input()
input_list = [int(i) for i in input().split(" ")]
bin_list = [bin(i)[2:] for i in input_list]
bin_count = []
mapped = {}
x = []
count = 0

# Getting the binary filter to sort
for num in bin_list:
    for i in num:
        count += int(i)
    bin_count.append(count)
    count = 0

# Grouping numbers according to their bitcount
for i in range(len(bin_count)):
    if bin_count[i] not in mapped.keys():
        mapped[bin_count[i]] = []
    mapped[bin_count[i]].append(input_list[i])

x = list(mapped.keys())
x.sort(reverse=True)
for i in x:
    mapped[i].sort()
    for j in mapped[i]:
        print(j, end=" ")
