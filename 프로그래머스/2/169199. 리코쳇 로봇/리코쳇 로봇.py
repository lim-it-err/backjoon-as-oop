from collections import deque
def get_agent_pos(board, N, M):
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                return (i, j)

def move(agent_pos, board, N, M, visited):
    is_valid = lambda x, y : 0<=x<N and 0<=y<M
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    candidate = []
    for dx, dy in zip(dxs, dys):
        cx, cy = agent_pos
        while is_valid(cx, cy):
            if not is_valid(cx+dx, cy+dy) or board[cx+dx][cy+dy] == "D":
                if not visited[cx][cy]:
                    candidate.append((cx, cy))
                break
            cx, cy = dx+cx, dy+cy
    return candidate
    
def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    is_valid = lambda x, y : 0<=x<N and 0<=y<N
    visited = [[False for _ in range(M)] for _ in range(N)]
    agent_pos = get_agent_pos(board, N, M)
    q = deque([(agent_pos[0], agent_pos[1], 0)])
    visited[agent_pos[0]][agent_pos[1]] = True
    while q:
        cur = q.popleft()
        x, y, cnt = cur
        if board[x][y] == "G":
            return cnt
        candidates = move((x, y), board, N, M, visited)
        for candidate in candidates:
            x, y = candidate
            visited[x][y] = True
            q.append((x, y, cnt+1))
    return -1