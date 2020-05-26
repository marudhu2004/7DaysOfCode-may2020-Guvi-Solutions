num = int(input().split(" ")[1])
num_list = [int(i) for i in input().split(" ")]
if num in num_list:
    print("yes")
else:
    print("no")
