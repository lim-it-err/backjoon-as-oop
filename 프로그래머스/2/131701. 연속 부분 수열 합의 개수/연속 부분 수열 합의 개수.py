
def solution(elements):
    answer = 0
    answer_dict = {}
    
    n = len(elements)
    elements *=2
    for i in range(2*n):
        for j in range(2*n):
            if i >=j:
                continue
            if i+n<j:
                continue
            _sum = sum(elements[i:j])
            answer_dict[_sum] = True
    answer = len(answer_dict.keys())
    return answer