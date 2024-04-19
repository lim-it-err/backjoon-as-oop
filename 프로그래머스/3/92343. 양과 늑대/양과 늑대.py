
from collections import deque, defaultdict
def dfs(info, adj_list, cur_node, num_sheep, num_wolf, visited):
    if visited[cur_node]:
        return -1
    if num_sheep <= num_wolf and num_sheep!=0 and num_wolf != 0:
        return -1
    visited[cur_node] = True
    N = len(info)
    info = info[:]
    max_value = -1
    if info[cur_node] == 0:
        info[cur_node] = -1
        visited = [False for _ in range(len(info))]
        visited[cur_node] =True
        for dst in adj_list[cur_node]:
            max_value = max(max_value, dfs(info, adj_list, dst, num_sheep+1, num_wolf, visited))
        return max(max_value, num_sheep)
    elif info[cur_node] == -1:
        for dst in adj_list[cur_node]:
            max_value = max(max_value, dfs(info, adj_list, dst, num_sheep, num_wolf, visited))
        return max(max_value, num_sheep)
    elif info[cur_node] == 1:
        info[cur_node] = -1
        for dst in adj_list[cur_node]:
            max_value = max(max_value, dfs(info, adj_list, dst, num_sheep, num_wolf+1, visited))
        return max(max_value, num_sheep)
def solution(info, edges):
    answer = 0
    visited = [False for i in range(len(info))]
    visited[0] = True
    lst = deque([(0, 1, 0, visited, info)])
    adj_list = defaultdict(list)
    for edge in edges:
        src, dst = edge
        adj_list[src].append(dst)
        adj_list[dst].append(src)
    

    return dfs(info, adj_list, 0, 0, 0, [False for _ in range(len(info))])