# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq

q = int(input())
heap = []
removed = set()

for _ in range(q):
    query = input().split()
    if query[0] == '1':
        x = int(query[1])
        heapq.heappush(heap, x)
    elif query[0] == '2':
        x = int(query[1])
        removed.add(x)
    else:
        while heap[0] in removed:
            removed.remove(heap[0])
            heapq.heappop(heap)
        print(heap[0])
