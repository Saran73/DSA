import heapq
list1 = [(1,"rai"),(2,"sia"),(3,"gia")]
heapq.heapify(list1)
print(list1)
for i in range(len(list1)):
    print(heapq.heappop(list1))