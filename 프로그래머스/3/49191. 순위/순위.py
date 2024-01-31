from collections import deque, defaultdict

def solution(n, results):
    answer = 0
    
    result_dict = defaultdict(list)
    result_reverse_dict = defaultdict(list)
    for result in results:
        src, dst = result
        result_dict[src-1].append(dst-1)
        result_reverse_dict[dst-1].append(src-1)
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        visited[i][i] = True
        q = deque([i])
        while q:
            element = q.pop()
            for next_visitor in result_dict[element]:
                if not visited[i][next_visitor]:
                    visited[i][next_visitor] = True
                    q.append(next_visitor)
    visited_temp = visited.copy()
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        visited[i][i] = True
        q = deque([i])
        while q:
            element = q.pop()
            for next_visitor in result_reverse_dict[element]:
                if not visited[i][next_visitor]:
                    visited[i][next_visitor] = True
                    q.append(next_visitor)
    visited_total = [sum(visit[:]) for visit in visited]
    for i in range(n):
        for j in range(n):
            visited[i][j] += visited_temp[i][j]
    for visit in visited:
        if all(visit):
            answer+=1
    return answer