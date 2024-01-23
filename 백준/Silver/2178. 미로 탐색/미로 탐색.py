import sys
from collections import deque
class B2178(object):
    def __init__(self, stdin):
        self.N, self.M = map(int, input().split(' '))
        self.arrayData = [[] for i in range(self.N)]
        self.visited = [[False for i in range(self.M)] for i in range(self.N)]
        self.distance = [[0 for i in range(self.M)] for i in range(self.N)]
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

        for i in range(self.N):
            self.arrayData[i] = list(map(int, input()))


    def bfs(self):
        q = deque()
        q.append((0, 0))
        self.distance[0][0] = 1
        while q:
            node = q.popleft()
            x, y = node
            if self.visited[x][y]:
                continue
            self.visited[x][y] = True

            for i in range(4):
                nx, ny = x+self.dx[i], y+self.dy[i]
                if nx < 0 or nx >= self.N or ny < 0 or ny >= self.M:
                    continue

                if self.arrayData[nx][ny] == 1:
                    q.append((nx, ny))
                    if not self.visited[nx][ny]:
                        self.distance[nx][ny] = self.distance[x][y]+1
            # print(q)

    def solution(self):
        self.bfs()
        # print(self.distance)
        print(self.distance[self.N-1][self.M-1])


if __name__ == "__main__":
    # import sys
    # import glob
    # print(glob.glob("B2178_tc/*.txt"))
    # for path in glob.glob("B2178_tc/*.txt"):
    #     print("ANSWER in", path)
    #     sys.stdin = open(path, "rt")
    #     b2178 = B2178(sys.stdin)
    #     b2178.solution()

    b2178 = B2178(sys.stdin)
    b2178.solution()