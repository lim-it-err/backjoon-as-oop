INF = 1e9
from collections import defaultdict
parent = []
def union(a, b):
    a = get_parent(a)
    b = get_parent(b)
    if (a < b):
        parent[b] = a
    else:
        parent[a] = b

def find(a, b):
    return get_parent(a) == get_parent(b)

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]
    
def solution(n, costs):
    global parent
    if n == 1:
        return 0
    parent = [i for i in range(n)]
    visited = [False for i in range(n)]
    answer = 0
    costs.sort(key=lambda x: x[2])
    
    idx = 0
    while True:
        cnt =0
        for i in range(n):
            if i ==0:
                continue
            if get_parent(i) == get_parent(i-1):
                cnt+=1
        if cnt == n-1:
            break
        src, dst, amount = costs[idx]
        if not find(src, dst):
            union(src, dst)
            visited[src], visited[dst] = True, True
            answer+=amount
            # print(src, dst, amount, visited)
        idx+=1
    # print(costs)
    # temp_answer = []
    # import random
    # for i in range(20):
    #     temp_answer.append([random.randint(0, 10), random.randint(0, 10), random.randint(0, 200)])
    # temp_answer.sort(key=lambda x: x[2])
    # print(temp_answer)
    return answer