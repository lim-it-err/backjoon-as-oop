def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col-1], -x[0]))
    result = []
    for i in range(row_begin, row_end+1):
        result.append(sum(d%i for d in data[i-1]))
    for res in result:
        answer ^= res
    return answer