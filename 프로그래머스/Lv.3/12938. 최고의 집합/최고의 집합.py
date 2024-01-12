def solution(n, s):
    if not s//n:
        return [-1]
    answer = [s//n for _ in range(n)]
    remain = s%n 
    if remain:
        for i in range(len(answer)-1, -1, -1):
            answer[i]+=1
            remain-=1
            if not remain:
                break
    
    return answer