from collections import deque

is_valid = lambda x, y: 0 <= x < N and 0 <= y < N if True else False
N, L, R = map(int, input().split())
country = []
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    country.append(list(map(int, input().split())))


def get_cluster(starting):
    cluster= []
    q = deque([starting])
    population = 0
    while q:
        x, y = q.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        cluster.append((x, y))

        population+=country[x][y]
        if is_valid(x+1, y) and not visited[x+1][y]:
            if L<=abs(country[x+1][y]- country[x][y])<=R:
                q.append((x+1, y))

        if is_valid(x-1, y) and not visited[x-1][y]:
            if L<=abs(country[x-1][y]- country[x][y])<=R:
                q.append((x-1, y))

        if is_valid(x, y+1) and not visited[x][y+1]:
            if L<=abs(country[x][y+1]- country[x][y])<=R:
                q.append((x, y+1))

        if is_valid(x, y-1) and not visited[x][y-1]:
            if L<=abs(country[x][y-1]- country[x][y])<=R:
                q.append((x, y-1))

    return len(cluster), cluster, population

cnt = 0
flag = False
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            country_len, country_list, population = get_cluster((i, j))
            if country_len == 1:
                continue
            for single_country in country_list:
                x, y = single_country
                visited[x][y] = True
                country[x][y] = population // country_len
                flag = True
    if not flag:
        print(cnt)
        break
    flag = False
    cnt+=1
