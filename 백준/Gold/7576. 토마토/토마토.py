from collections import deque


def _coordinate_validate(x, y, sizex, sizey):
    if x < 0 or x >= sizex or y < 0 or y >= sizey:
        return False
    return True


class B7576(object):
    def __init__(self, stdin = None):
        self.N, self.M = list(map(int, input().split(' ')))
        self.visited = [[False for i in range(self.N)] for i in range(self.M)]
        self.discovered = [[False for i in range(self.N)] for i in range(self.M)]
        self.inputdata = self._get_input(stdin)
        self.dx, self.dy = [1, -1, 0, 0], [0, 0, 1, -1]  # EWSN

    def __call__(self, *args, **kwargs):
        import time
        s_t = time.time()
        self.sol_bfs()
        # print(time.time()-s_t)

    #시간초과
    def sol_bfs(self):
        q = deque([(i, j) for i in range(self.M) for j in range(self.N) if self.inputdata[i][j] == 1])
        q_iter = len(q)
        iteration = -1
        while q and q_iter:
            if q:
                x, y = q.popleft()
                if self.visited[x][y]:
                    continue
                self.visited[x][y] = True
                self.inputdata[x][y] = 1
                for i in range(4):
                    nx, ny = x + self.dx[i], y + self.dy[i]
                    if not _coordinate_validate(nx, ny, self.M, self.N):
                        continue
                    if self.inputdata[nx][ny] == 0 and not self.discovered[nx][ny]:
                        q.append((nx, ny))
                        self.discovered[nx][ny] =True

            # Batch Finished
            q_iter -= 1
            # print(q_iter, len(q), q)
            if q_iter == 0:
                q_iter = len(q)
                iteration += 1
                # print(iteration, self.inputdata, self.visited)
        if any((i, j) for i in range(self.M) for j in range(self.N) if self.inputdata[i][j] == 0):
            print(-1)
            return
        print(iteration)

    def _get_input(self, stdin):
        inputdata = []
        for i in range(self.M):
            _line = list(map(int, input().split(' ')))
            inputdata.append(_line)
        return inputdata


if __name__ == "__main__":
    USER_INPUT = True
    if USER_INPUT:
        b7576 = B7576()
        b7576()

    else:
        import sys
        import glob
        print(glob.glob("tc/*.txt"))
        for path in glob.glob("tc/*.txt"):
            print("ANSWER in", path)
            sys.stdin = open(path, "rt")
            b7576 = B7576(sys.stdin)
            b7576()


