from typing import Tuple
def calc(src, dst):
    horizontal =  src[1]-dst[1]
    vertical = src[0]-dst[0]
    typ = "not linear"
    if not horizontal or not vertical:
        typ = "linear"
    return abs(horizontal)+abs(vertical), typ

def find_user(places):
    _lst = []
    for i in range(len(places)):
        for j in range(len(places)):
            if places[i][j] == "P":
                _lst.append((i, j))
    return _lst

def solution(places):
    from itertools import combinations
    answer = []
    flag = False
    for place in places:
        user_pos = find_user(place)
        for pair in combinations(user_pos, 2):
            src, dst = pair
            distance, typ = calc(pair[0], pair[1])
            #대각선
            if distance >2:
                continue
            print(pair, distance, typ)
            if distance == 2 and typ == "not linear":
                if place[dst[0]][src[1]] == "X" and place[src[0]][dst[1]] == "X":
                    continue
            elif distance == 2 and typ == "linear":

                if place[(src[0]+dst[0])//2][(src[1]+dst[1])//2] == "X":
                    continue
            flag = True
            answer.append(0)
            break
        if not flag:
            answer.append(1)
        flag = False

    return answer