# 누적합
# 1. 쿼리를 역으로 돌리면서
# 2. 후보 영역이 벽과 마닿고, 그에 수직하는 쿼리가 발생했을때는 그에 상응하는 직사각형을 생성한다.
# 3. 아닐 경우, 직사각형을 평행이동한다. 
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

def is_conflict(left, right, pos, n, m, amount):
    if pos == 2: # Up
        if left[0]-amount < 0:
            return left[0]+1
    if pos == 3: # Down
        if right[0]+amount > n-1:
            return n-right[0]
    if pos == 0: # Left
        if left[1] -amount < 0:
            return left[1]+1
    if pos == 1: # right
        if right[1] +amount > m-1:
            return m-right[1]
    return False
#TODO : Overlap 함수 연습.

def overlap(a_l, a_r, b_l, b_r):
    x_min = max(a_l[0], b_l[0])
    x_max = min(a_r[0], b_r[0])
    y_min = max(a_l[1], b_l[1])
    y_max = min(a_r[1], b_r[1])
    if x_min>x_max or y_min > y_max:
        return False, -1, -1
    return True, (x_min, y_min), (x_max, y_max)
    
def move_rectangle(left, right, pos, amount, n, m):
    ret = True
    lx, ly = left
    rx, ry = right
    n_left = (lx+dxs[pos]*amount, ly+dys[pos]*amount)
    n_right = (rx+dxs[pos]*amount, ry+dys[pos]*amount)
    ret, n_left, n_right = overlap(n_left, n_right, (0, 0), (n-1, m-1))
        
    return ret, n_left, n_right

def increase_rectangle(left, right, pos, amount, n, m):
    lx, ly = left
    rx, ry = right
    if pos ==0: # Left
        left, right = (lx, max(ly-amount, 0)), (rx, ry)
    if pos ==2: # Up
        left, right = (max(lx-amount, 0), ly), (rx, ry)
    if pos ==1: # Right
        left, right = (lx, ly), (rx, min(m-1, ry+amount))
    if pos ==3 : # Down
        left, right = (lx, ly), (min(n-1, rx+amount), ry)
    return left, right

def solution(n, m, x, y, queries):
    answer = -1
    queries.reverse() #O(n)
    left, right = (x, y), (x, y)
    opposite = {0: 1, 1:0, 2:3, 3:2}
    for query in queries:
        pos, amount = query
        opposite_pos = opposite[pos]
        margin = is_conflict(left, right, pos, n, m, 1)
        if margin:
            left, right = increase_rectangle(left, right, opposite_pos, amount, n, m)
            # print("11",pos, left, right, margin)

            # ret, left, right = move_rectangle(left, right, opposite_pos, amount-margin, n, m)
            # print("12",ret, pos, left, right, amount-margin)

            # if ret == False:
                # return 0
        else:
            ret, left, right = move_rectangle(left, right, opposite_pos, amount, n, m)
            # print("2", pos,left, right)
            if ret == False:
                return 0
    # print(left, right)
    return (abs(left[0]-right[0])+1)*(abs(left[1]-right[1])+1)