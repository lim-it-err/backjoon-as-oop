from collections import defaultdict, deque
def number_of_nodes(n, wires):
    graph = defaultdict(list)
    for wire in wires:
        src, dst = wire
        graph[src].append(dst)
        graph[dst].append(src)
    visited = {k: False for k in graph.keys()}
    for area_count in range(2):
        tmp_cnt = 0
        for k in visited:
            if visited[k] == True:
                tmp_cnt+=1
        if tmp_cnt == n:
            return 1e9 # area is not splitted
        q = deque([list(graph.keys())[0]])
        while q:
            cur = q.popleft()
            for next_cur in graph[cur]:
                if visited[next_cur]:
                    continue
                visited[next_cur] = True
                q.append(next_cur)
        if area_count == 0:
            tmp_cnt = 0
            for k in visited:
                if visited[k] == True:
                    tmp_cnt+=1
    return abs(n-tmp_cnt*2)

def solution(n, wires):
    answer = 1e9
    for i in range(len(wires)):
        a = number_of_nodes(n, wires[:i]+wires[i+1:])
        answer = min(abs(a), answer)
        # print(i, a)
    return answer 