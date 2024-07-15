N = int(input())
cards = []
for i in range(N):
    cards.append(int(input()))

import heapq
import sys

sum = 0
hq = []
for i in range(0, len(cards)):
    heapq.heappush(hq, cards[i])
if N == 1:
    print(0)
    sys.exit()

while True:
    num1 = heapq.heappop(hq)
    num2 = heapq.heappop(hq)
    sum += (num1 + num2)
    if len(hq) == 0:
        break
    heapq.heappush(hq, num1 + num2)

print(sum)