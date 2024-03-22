from collections import deque
maximum_area = -1
def dfs(k, dungeons, cnt):
    global maximum_area
    flag = False
    for i,dungeon in enumerate(dungeons):
        src, cost = dungeon
        if src<=k:
            dfs(k-cost, dungeons[:i]+dungeons[i+1:], cnt+1)
            flag = True
    if not flag:
        maximum_area = max(cnt, maximum_area)
def solution(k, dungeons):
    global maximum_area
    answer = -1
    dfs(k, dungeons, 0)
    return maximum_area