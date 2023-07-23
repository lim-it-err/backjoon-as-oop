import heapq
from collections import defaultdict

N, M, K, X = map(int, input().split())
info = defaultdict(list)
distance = [1e9 for i in range(N)]

for i in range(M):
    src, dst = map(int, input().split())
    info[src-1].append(dst-1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in info[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
dijkstra(X-1)
# print(distance)
flag = 0
for i in range(N):
    if distance[i] == K:
        print(i+1)
        flag = 1
if not flag:
    print(-1)

