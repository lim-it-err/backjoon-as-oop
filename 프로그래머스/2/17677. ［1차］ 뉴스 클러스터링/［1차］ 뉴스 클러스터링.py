def to_lower(letter):
    if ord("A")<=ord(letter)<=ord("Z"):
        return chr(ord(letter)-ord("A")+ord("a"))
    return letter
def is_letter(letters):
    for letter in letters:
        if not (ord("A")<=ord(letter)<=ord("Z") or ord("a")<=ord(letter)<=ord("z")):
            return False
    return True
def solution(str1, str2):
    answer = 0
    str1 = "".join(list(map(to_lower, str1)))
    str2 = "".join(list(map(to_lower, str2)))
    from collections import defaultdict
    dic1, dic2, dic3 = defaultdict(int), defaultdict(int), defaultdict(int)
    for i in range(len(str1)-1):
        if is_letter(str1[i:i+2]):
            dic1[str1[i:i+2]]+=1
            dic3[str1[i:i+2]]+=1

    for i in range(len(str2)-1):
        if is_letter(str2[i:i+2]):
            dic2[str2[i:i+2]]+=1
            dic3[str2[i:i+2]]+=1

    x, y = 0, 0
    for key in dic3:
        if key in dic1 and key in dic2:
            x += min(dic1[key], dic2[key])
        y+=max(dic1[key], dic2[key])
    if y == 0:
        return 65536
    return int(x/y*65536)