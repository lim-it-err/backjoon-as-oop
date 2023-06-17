import re
def solution(s):
    answer = []
    counter = {}
    s = s[1:-1]
    splitted = re.split(r'{|}|,', s)
    for value in splitted:
        if value == "":
            continue
        if value not in counter:
            counter[value] = 1
        else:
            counter[value]+=1
    counter = sorted(counter.items(), key=lambda x:-x[1])
    for x, y in counter:
        answer.append(int(x))
    return answer