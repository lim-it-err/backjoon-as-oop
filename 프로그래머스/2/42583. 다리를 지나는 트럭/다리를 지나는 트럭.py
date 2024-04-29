from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)
    process_q = deque()
    cur_weight = 0
    t = 1
    while True:
        while process_q:
            if process_q[0][1] + bridge_length ==t:
                local_weight = process_q.popleft()
                cur_weight-= local_weight[0]
            else:
                break
        if q:
            if cur_weight + q[0] <= weight:
                local_weight = q.popleft()
                process_q.append((local_weight, t))
                cur_weight += local_weight
        if not q and not process_q:
            return t
        t+=1
        
    return -333