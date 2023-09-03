N, H = map(int, input().split())
input_walls = [int(input()) for _ in range(N)]

from_down = [0] * (H + 1)
from_up = [0] * (H + 1)

for i, wall in enumerate(input_walls):
    if i % 2:
        from_down[wall] += 1
    else:
        from_up[wall] += 1

_sum = 0
sum_from_down, sum_from_up = [], []
for num in from_down:
    _sum += num
    sum_from_down.append(_sum)
_sum = 0
for num in from_up:
    _sum += num
    sum_from_up.append(_sum)

min_wall = 9999999
cnt = 0
for i in range(H):
    wall = (
        sum_from_down[-1] - sum_from_down[i] + sum_from_up[-1] - sum_from_up[H - i - 1]
    )
    if wall < min_wall:
        cnt = 1
        min_wall = wall
    elif wall == min_wall:
        cnt += 1
print(min_wall, cnt)

