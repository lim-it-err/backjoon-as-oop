from typing import List
import math
def solution(s):
    answer = []
    letter = [*s]
    N = len(s)
    prev_cur = ""
    
    for unit in range(1, N+1):
        local_answer = 0
        doubled = 0
        prev_cur = None
        for j in range(math.ceil(N/unit)):
            if (j+1)*(unit)<N:
                cur = s[j*unit:(j+1)*(unit)]
            else:
                cur = s[j*unit:]
            if prev_cur:

                if prev_cur == cur:
                    doubled += 1
                    continue
                else:
                    if doubled:
                        local_answer +=len(str(doubled+1))
                    doubled = 0
            local_answer+=len(cur)
            prev_cur = cur
        if doubled:
            local_answer+=len(str(doubled+1))
        answer.append(local_answer)
    return min(answer)