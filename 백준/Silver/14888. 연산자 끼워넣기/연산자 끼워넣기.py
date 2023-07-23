N = int(input())
numbers = list(map(int, input().split()))
choices = list(map(int, input().split()))

max_value = -1e10
min_value = 1e10
def dfs(number, choices_left, value):
    global max_value, min_value
    # print(number, choices_left, value)
    if number == N:
        max_value = max(max_value, value)
        min_value = min(min_value, value)

    plus, minus, multiply, divide = choices_left
    if plus > 0:
        dfs(number+1, [plus-1, minus, multiply, divide], value+numbers[number])
    if minus > 0:
        dfs(number + 1, [plus, minus - 1, multiply, divide], value - numbers[number])
    if multiply > 0:
        dfs(number + 1, [plus, minus, multiply - 1, divide], value * numbers[number])
    if divide > 0:
        if value<0:
            dfs(number + 1, [plus, minus, multiply, divide - 1], -(-value // numbers[number]))
        else:
            dfs(number + 1, [plus, minus, multiply, divide - 1], value // numbers[number])

dfs(1, choices, numbers[0])
print(int(max_value))
print(int(min_value))


#3
#1 2 1
#0 1 0 1