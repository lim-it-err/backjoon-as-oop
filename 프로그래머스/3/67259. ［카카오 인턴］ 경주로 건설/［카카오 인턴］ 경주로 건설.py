from collections import deque
STRAIGHT_COST = 100
CONOR_COST = 500
MAX_WON = 1e9
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
def solution(board):
    answer = 0
    memo = [[[MAX_WON, MAX_WON] for _ in range(len(board))] for _ in range(len(board))]
    memo[0][0][0], memo[0][0][1] = 0, 0
    q = deque()
    q.extend([((0, 0), 0), ((0, 0), 1), ((0, 0), 2), ((0, 0), 3)])
    while q:
        pos, di= q.popleft()

        if pos == (len(board)-1, len(board)-1):
            answer = min(memo[len(board)-1][len(board)-1])
        x, y = pos

        for i in range(4):
            nx, ny = x+dxs[i], y+dys[i]
            if not (0<=nx<len(board) and  0<=ny<len(board)):
                continue
            if board[nx][ny] == 1:
                continue
            if (di+2)%4 == i: # Opposite Way
                continue
            if i % 2: #VERTICAL
                if min(memo[x][y][0]+STRAIGHT_COST+CONOR_COST, memo[x][y][1] + STRAIGHT_COST) < memo[nx][ny][1] :
                    memo[nx][ny][1]  = min(memo[x][y][0]+STRAIGHT_COST+CONOR_COST, memo[x][y][1] + STRAIGHT_COST)
                    q.append(((nx, ny), i))

            else:
                if min(memo[x][y][1]+STRAIGHT_COST+CONOR_COST, memo[x][y][0] + STRAIGHT_COST) < memo[nx][ny][0] :
                    memo[nx][ny][0]  = min(memo[x][y][1]+STRAIGHT_COST+CONOR_COST, memo[x][y][0] + STRAIGHT_COST)
                q.append(((nx, ny), i))
    # print(memo)
    return min(memo[len(board)-1][len(board)-1])