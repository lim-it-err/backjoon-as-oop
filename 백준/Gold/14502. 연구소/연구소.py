import copy
from itertools import combinations


N, M = map(int, input().split())
is_valid = lambda i, j: 0 <= i < N and 0 <= j < M if True else False

space = [[0 for _ in range(M)] for _ in range(N)]
virus_space = []
wall_space = []
empty_space= []
for i in range(N):
    space[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        if space[i][j]==0:
            empty_space.append((i, j))
        elif space[i][j]==1:
            wall_space.append((i, j))
        elif space[i][j]==2:
            virus_space.append((i, j))


class Lab():
    def __init__(self, init_map, empty, wall, virus):
        self.map = init_map
        self.empty = empty
        self.virus = virus

    def new_wall(self):
        def get_sublists(lst, k):
            return list(combinations(lst, k))

        return get_sublists(self.empty, 3)

    def safe(self, added_walls):
        local_map = copy.deepcopy(self.map)
        for wall in added_walls:
            local_map[wall[0]][wall[1]] = 1
        for single_virus in self.virus:
            self._spread(local_map, single_virus)
        area = 0
        for i in range(N):
            for j in range(M):
                if local_map[i][j] == 0:
                    area+=1
        return area

    def _spread(self, space, starting):
        vx, vy = starting
        space[vx][vy] = 2
        if is_valid(vx+1, vy):
            if space[vx+1][vy] == 0:
                self._spread(space, (vx+1, vy))
        if is_valid(vx-1, vy):
            if space[vx-1][vy] == 0:
                self._spread(space, (vx-1, vy))
        if is_valid(vx, vy+1):
            if space[vx][vy+1] == 0:
                self._spread(space, (vx, vy+1))
        if is_valid(vx, vy-1):
            if space[vx][vy-1] == 0:
                self._spread(space, (vx, vy-1))


lab = Lab(space, empty_space, wall_space, virus_space)

added_wall_candid = lab.new_wall()
max_safezone = -1
for wall in added_wall_candid:
    max_safezone = max(max_safezone, lab.safe(wall))
print(max_safezone)