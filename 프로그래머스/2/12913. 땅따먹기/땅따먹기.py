def solution(land):
    answer = 0
    prev_dp = [-1 for i in range(4)]
    dp = [-1 for i in range(4)]
    N = len(land)
    for i in range(N):
        if i == 0:
            dp = land[0]
            
        else:
            for j in range(4):
                candidates = [prev_dp[k]+land[i][j] for k in range(4) if k!=j]
                dp[j] = max(candidates)
        prev_dp = dp[:]
    return max(dp)