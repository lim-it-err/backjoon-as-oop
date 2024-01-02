from itertools import permutations

def matches(single_user, single_ban):
    up, bp = 0, 0 #user pointer, ban pointer
    if len(single_user) != len(single_ban):
        return False
    while up < len(single_user):
        if single_ban[bp] == "*":
            up +=1
            bp +=1
            continue
        if single_user[up] != single_ban[bp]:
            return False
        up += 1
        bp += 1

    return True
    
def solution(user_id, banned_id):
    answer, cnt = [], 0
    for users in permutations(user_id, len(banned_id)):
        _banned = []
        for ban in banned_id:
            for user in users:
                if user in _banned:
                    continue
                if matches(user, ban):
                    cnt +=1
                    _banned.append(user)
                    break
        if cnt == len(banned_id):
            if set(_banned) not in answer:
                answer.append(set(_banned))
        cnt = 0
    # test_matches("string", "st*ing")
    return len(answer)

def test_permutation(user_id):
    print(list(permutations(user_id, 3)))
    
def test_matches(str1, str2):
    print(matches(str1, str2))
    