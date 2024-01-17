from collections import deque, defaultdict

def solution(n, edge):
    answer = 0
    vertex_graph = defaultdict(list)
    vertex_count = [1e9 for _ in range(n+1)]
    for single_edge in edge:
        src, dst = single_edge
        vertex_graph[src].append(dst)
        vertex_graph[dst].append(src)

    q = deque([1])
    vertex_count[0] = 0
    vertex_count[1] = 0
    while q:
        dst = q.popleft()
        for edge in vertex_graph[dst]:
            if vertex_count[edge] != 1e9:
                continue
            vertex_count[edge] = vertex_count[dst] + 1
            q.append(edge)

    return vertex_count.count(max(vertex_count))