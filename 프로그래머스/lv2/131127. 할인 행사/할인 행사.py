from collections import Counter

def check_avail(criteria, dst):
    for i, (key, value) in enumerate(criteria.items()):
        if not key in dst:
            return False
        if value > dst[key]:
            return False
    return True
        
def solution(want, number, discount):
    answer = 0
    N = len(discount)
    want_freq = {k:v for k, v in zip(want, number)}
    discount_freq = Counter(discount[0:10])
    for i in range(N-10+1):
        if check_avail(want_freq, discount_freq):
            answer+=1
        if i == N-10:
            break

        discount_freq[discount[i]]-=1
        if discount[i+10] not in discount_freq:
            discount_freq[discount[i+10]]=0
        discount_freq[discount[i+10]]+=1

    return answer