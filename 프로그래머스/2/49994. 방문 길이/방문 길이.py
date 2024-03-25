visited = [[[False for _ in range(12)] for _ in range(12)] for _ in range(2)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
dir_map = {"U": 2, "R": 1, "D": 0, "L": -1}
is_valid = lambda x, y, vec: True if -5<=x+dxs[dir_map[vec]]<=5 and -5<=y+dys[dir_map[vec]]<=5 else False
def solution(dirs):
    answer = 0
    from collections import deque
    curx, cury = 0, 0
    for i in range(len(dirs)):
        if not is_valid(curx, cury, dirs[i]):
            print(f"Skipping {i}")
            continue
        nxt_curx = curx+ dxs[dir_map[dirs[i]]]
        nxt_cury = cury + dys[dir_map[dirs[i]]]
        print(curx, cury)
        print(nxt_curx, nxt_cury)
        print("==")
        if abs(nxt_curx-curx): # 가로 이동
            visited[0][min(curx, nxt_curx)][cury] = True
        else:
            visited[1][curx][min(cury, nxt_cury)]= True
        curx, cury = nxt_curx, nxt_cury
    return sum(sum(sum(v) for v in visit[:]) for visit in visited[:])