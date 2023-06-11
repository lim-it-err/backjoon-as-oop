def get_divisor(num: int):
    lst = []
    i = 1
    while i*i <= num:
        if not num%i:
            lst.append(i)
        i+=1
    return lst


def solution(brown, yellow):
    divisor = get_divisor(brown+yellow)
    for divise in divisor:
        other_divise = (yellow+brown) // divise
        if (other_divise+divise -2) *2 == brown:
            return [other_divise, divise]
