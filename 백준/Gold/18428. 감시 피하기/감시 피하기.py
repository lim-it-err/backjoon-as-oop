from collections import deque
import copy
from itertools import combinations
is_valid = lambda x, y: 0 <= x < N and 0 <= y < N if True else False
N = int(input())
empty_space = []
teachers = []
classroom = []
for i in range(N):
    classroom.append(input().split())

for i in range(N):
    for j in range(N):
        if classroom[i][j] == "X":
            empty_space.append((i, j))
        elif classroom[i][j] == "T":
            teachers.append((i, j))
def is_observed(obstacles):
    _classroom = copy.deepcopy(classroom)
    for obstacle in obstacles:
        x, y = obstacle
        _classroom[x][y] = "O"
    for teacher in teachers:
        x, y = teacher
        cur = 0
        while is_valid(x-cur, y):
            if _classroom[x-cur][y] == "O":
                break
            if _classroom[x-cur][y] == "S":
                return True
            cur+=1
        cur = 0

        while is_valid(x+cur, y):
            if _classroom[x+cur][y] == "O":
                break
            if _classroom[x+cur][y] == "S":
                return True
            cur+=1
        cur = 0

        while is_valid(x, y-cur):
            if _classroom[x][y-cur] == "O":
                break
            if _classroom[x][y-cur] == "S":
                return True
            cur+=1
        cur = 0

        while is_valid(x, y+cur):
            if _classroom[x][y+cur] == "O":
                break
            if _classroom[x][y+cur] == "S":
                return True
            cur+=1
    return False
obstacles_candidate = list(combinations(empty_space, 3))
flag = 0
for obstacles in obstacles_candidate:
    if not is_observed(obstacles):
        flag = 1
        print("YES")
        break
if not flag:
    print("NO")

