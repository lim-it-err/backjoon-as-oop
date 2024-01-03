from collections import deque
direction_str = ["d", "l", "r", "u"]
dxs, dys = [1, 0, 0, -1], [0, -1, 1, 0] #down, left, right, up

def get_distance(src, dst):
    return abs(src[0]-dst[0])+abs(src[1]-dst[1])
def solution(n, m, x, y, r, c, k):
    def is_valid(n, m, ptr):
        if 0<=ptr[0]<n and 0<=ptr[1]<m:
            return True
        return False
    
    x, y, r, c = x-1, y-1, r-1, c-1
    
    s = deque([((x, y), 0, "")])
    while s:
        cur_pos, attempts, route = s.popleft()
        curx, cury = cur_pos
        if attempts>k:
            continue
        if (curx, cury) == (r, c) and attempts == k:
            return route
        if get_distance((curx, cury), (r, c))<attempts-k:
            "impossible"
        for direction in range(4): #down, left, right, up
            if not is_valid(n, m, (curx+dxs[direction], cury+dys[direction])):
                continue
            nextx, nexty = curx+dxs[direction], cury+dys[direction]
            if get_distance((nextx, nexty), (r, c)) + attempts + 1 > k:
                continue

            s.append(((nextx, nexty), attempts+1, route+direction_str[direction]))
            break
    return "impossible"