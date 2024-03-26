def get_sum(n):
    return sum(map(int, str(bin(n))[2:]))
def solution(n):
    answer = 0
    target_sum = get_sum(n)
    n+=1
    while get_sum(n) != target_sum:
        n+=1
    return n