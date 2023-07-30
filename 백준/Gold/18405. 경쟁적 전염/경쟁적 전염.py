from collections import deque

N, M = map(int, input().split())
virus_map = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
is_valid = lambda x, y: 0 <= x < N and 0 <= y < N if True else False

virus_lst = []
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
for i in range(N):
    for j in range(N):
        if virus_map[i][j] != 0:
            virus_lst.append((virus_map[i][j], i, j))

virus_lst.sort()
q = deque(virus_lst)
second = 0
while q:
    if second == S:
        break
    for _ in range(len(q)):
        virus_type, x, y = q.popleft()
        for i in range(4):
            if is_valid(x+dx[i], y+dy[i]) and virus_map[x+dx[i]][y+dy[i]] == 0:
                virus_map[x + dx[i]][y + dy[i]] = virus_type
                q.append((virus_type, x + dx[i], y + dy[i]))
    second+=1
print(virus_map[X-1][Y-1])

