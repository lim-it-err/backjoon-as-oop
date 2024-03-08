def get_area(src, dst):
    return (src+dst)/2
def is_odd(value):
    return value%2
value = []
area = []
def solution(k, ranges):
    answer = []
    ret, prev_ret = k, k
    while ret!=1:
        prev_ret = ret
        if is_odd(ret):
            ret = ret*3+1
        else:
            ret = ret//2
        value.append(ret)
        area.append(get_area(prev_ret, ret))
    print(area)
    for _range in ranges:
        src, dst = _range
        if len(area)+dst<src or src>len(area):
            answer.append(-1)
            continue
        if dst == 0:
            answer.append(sum(area[src:]))
            continue
        answer.append(sum(area[src:dst]))
    return answer
