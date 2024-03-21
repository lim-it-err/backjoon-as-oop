result_arr = []
max_result = 0
def get_score(arr, apeach):
    score_lion, score_apeach = 0, 0
    internal_score = [10-i for i in range(11)]
    for i in range(11):
        _ar, _is, _ap = arr[i], internal_score[i], apeach[i]
        if _ar == 0 and _ap == 0:
            continue
        if _ar>_ap:
            score_lion += _is
        else:
            score_apeach += _is
    return score_lion, score_apeach


def dfs(info, result, n_left, apeach_score):
    global result_arr, max_result
    if n_left <0:
        return
    if len(result) == 11:
        result[10] = n_left
        score = get_score(result, apeach_score)   
        if max_result < score[0]-score[1]:
            max_result = score[0]-score[1]
            result_arr = [result]
        elif max_result == score[0]- score[1] and score[0]!=score[1]:
            result_arr.append(result)
        return
            
    apeach_choice = info[0]
    dfs(info[1:], result+[apeach_choice+1], n_left-apeach_choice-1, apeach_score)
    dfs(info[1:], result+[0], n_left, apeach_score)
    
    return max_result

def solution(n, info):
    global result_arr
    dfs(info, [], n,info)
    if result_arr == []:
        return [-1]
    if len(result_arr)>1:
        reverse_result_arr = []
        for arr in result_arr:
            arr.reverse()
            reverse_result_arr.append(arr)
        result_arr = max(reverse_result_arr)
        result_arr.reverse()
        return result_arr
    return result_arr[0]