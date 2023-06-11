def negative_parser(n: str):
    if n[0].startswith('-'):
        return int(n[1:]) * -1
    return int(n)

def solution(s):
    lst = s.split(' ')
    lst = list(map(negative_parser, lst))
    lst.sort()
    return f'{lst[0]} {lst[-1]}'