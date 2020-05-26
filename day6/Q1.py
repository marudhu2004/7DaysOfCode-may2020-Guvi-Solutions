import queue

s = input().split(" ")
q = queue.Queue()
for i in s[::-1]:
    q.put(i)
for i in range(q.qsize()):
    print(q.get(), end=" ")
