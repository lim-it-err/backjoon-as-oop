def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    cur_max = 0
    for target in targets:
        src, dst = target
        if src<cur_max:
            continue
        cur_max = dst
        answer+=1
    return answer
