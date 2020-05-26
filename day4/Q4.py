# your code goes here

node_count = int(input())
nodes = input("").split(" ")
final_list = []

for node in nodes:
    node = int(node)
    if node not in final_list:
        final_list.append(node)

for i in final_list[:-1]:
    print(i, end=" ")

print(final_list[-1])
