N = int(input())
M = int(input())
apple_map = [[False for _ in range(N)] for _ in range(N)]
history = {}
for i in range(M):
    x, y = map(int, input().split())
    apple_map[x-1][y-1] = True

L = int(input())
for i in range(L):
    time, direction = input().split()
    history[int(time)] = direction

class Snake:
    def __init__(self, N):
        self.N = N
        self.body = [(0, 0)]
        self.direction = 0 #0 = East, 1=South, 2 = West ...

    def next_head(self):
        x, y = self.body[-1]
        if self.direction == 0:
            return (x, y+1)
        elif self.direction == 1:
            return (x+1, y)
        elif self.direction == 2:
            return (x, y-1)
        elif self.direction == 3:
            return (x-1, y)
        else:
            raise TypeError("direction not expected")

    def step(self, position, apple):
        self.body.append(position)
        if not apple:
            self.body.pop(0)

    def change_direction(self, direction):
        if direction == "L": # Left
            self.direction = (self.direction-1)%4
        elif direction == "D":
            self.direction = (self.direction+1)%4
        else:
            raise KeyError("Direction Type not expected")

    def collide(self, position):
        x, y = position
        if x >= self.N or y >= self.N or x < 0 or y < 0:
            return True
        if (x, y) in self.body:
            return True
        return False

cnt = 0
snake = Snake(N)
while True:
    cnt+=1
    next_pos = snake.next_head()
    if snake.collide(next_pos): # Collision Validation
        print(cnt)
        break
    if apple_map[next_pos[0]][next_pos[1]]:
        apple_map[next_pos[0]][next_pos[1]] = False
        snake.step(next_pos, apple=True)
    else:
        snake.step(next_pos, apple=False)
    if cnt in history.keys():
        snake.change_direction(history[cnt])
