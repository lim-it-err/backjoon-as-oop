#Assumption: Delete most overlapped area. -> Wrong?
from collections import defaultdict

def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[1])
    recent_cam = -30001
    for route in routes:
        src, dst = route
        if src<= recent_cam<=dst:
            continue
        else:
            recent_cam = dst
            answer+=1
            
    return answer