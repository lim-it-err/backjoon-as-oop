answer = []

def solution(n, src=1, dst=3, via=2):
    global answer
    if n ==1:
        answer.append([src, dst])
        return
    solution(n-1, src=src, dst=via, via=dst)
    answer.append([src, dst])
    solution(n-1, src=via, dst=dst, via=src)
    return answer