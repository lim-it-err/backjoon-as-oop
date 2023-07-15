def solution(s: str):
    cnt = 0
    flag = s[0]
    for i in range(len(s)):
        if flag != s[i]:
            cnt+=1
            flag = s[i]
    print((cnt+1)//2)
s = input()
solution(s)