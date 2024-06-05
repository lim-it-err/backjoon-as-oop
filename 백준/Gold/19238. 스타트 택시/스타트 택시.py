from collections import deque

memo = {}

def find_customer(src, passenger_map, map, N):
    x, y = src
    visited = [[False for i in range(N)] for i in range(N)]
    q = deque([(x, y)])
    candidate = []
    distance = 0
    while q:
        d = len(q)
        for _ in range(d):
            i, j = q.popleft()
            if passenger_map[i][j]:
                candidate.append((i, j))
            for ele in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ele_x, ele_y = ele
                m, n = ele_x+i, ele_y+j
                if not 0 <= m < N or not 0 <= n < N or map[m][n] or visited[m][n]:
                    continue
                visited[m][n] = True
                q.append((m, n))
        if candidate:
            return distance, candidate

        distance+=1
    return None, None


def cal_passenger_distance(src, dst, map, N):
    src, dst = tuple(src), tuple(dst)

    def action(i, j, map, N):
        try:
            return memo[((i, j), dst)]
        except:
            pass
        if not 0 <= i < N or not 0 <= j < N:
            return 0
        if map[i][j]:
            return 0
        if visited[i][j]:
            return 0
        q.append((i, j))
        visited[i][j] = True
        return 0
    distance = 0
    src, dst = tuple(src), tuple(dst)
    q = deque()
    visited = [[0 for i in range(N)] for i in range(N)]
    q.append(src)
    if src == dst:
        return 0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if (x, y) == dst:
                return distance
            ret = action(x + 1, y, map, N)
            ret+= action(x - 1, y, map, N)
            ret += action(x, y + 1, map, N)
            ret += action(x, y - 1, map, N)
            if ret:
                memo[(src, dst)] = ret+1
                memo[(dst, src)] = ret+1
                return ret+1
        distance+=1

class Taxi:
    def __init__(self, N, M, fuel):
        self.N, self.M, self.fuel = N, M, fuel
        self.map = [list(map(int, input().split())) for i in range(self.N)]
        self.start, self.end = list(map(int, input().split(' ')))
        self.routes = [list(map(int, input().split())) for i in range(self.M)]
        self.passenger_map = [[False for _ in range(self.N)] for _ in range(self.N)]
        self.route = {}
        for route in self.routes:
            a, b, c, d = route
            self.route[(a - 1, b - 1)] = [c - 1, d - 1]
            self.passenger_map[a-1][b-1] = True
        self.start, self.end = self.start - 1, self.end - 1

    def move(self, src):
        x, y = src
        self.passenger_map[x][y] = False
        dst = self.route[tuple(src)]
        del self.route[tuple(src)]

        return dst, cal_passenger_distance(src, dst, self.map, self.N)

    def select_passenger(self, now):
        distance, candidate = find_customer(now, self.passenger_map, self.map, self.N)
        if distance == None:
            return -1, -1
        candidate.sort()
        return candidate[0], distance

    def gain_fuel(self, before_pass_distance, after_pass_distance):
        if self.fuel - before_pass_distance - after_pass_distance < 0:
            return False
        self.fuel += after_pass_distance * 2 - before_pass_distance - after_pass_distance
        return True

    def interface(self):
        taxi_pos = [self.start, self.end]
        for i in range(self.M):
            taxi_x, taxi_y = taxi_pos
            passenger_pos, before_pass_distance = self.select_passenger([taxi_x, taxi_y])
            if passenger_pos == -1:
                return -1
            taxi_pos, after_pass_distance = self.move(passenger_pos)
            if after_pass_distance == None:
                return -1
            if not self.gain_fuel(before_pass_distance, after_pass_distance):
                return -1
        return self.fuel


if __name__ == "__main__":
    N, M, fuel = list(map(int, input().split(' ')))
    taxi = Taxi(N, M, fuel)
    print(taxi.interface())
