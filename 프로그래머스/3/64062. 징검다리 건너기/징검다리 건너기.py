from collections import deque

class MaxStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.len = 0
        self.data = deque()
        self.idx = 0
        
    def add(self, data):
        pack = (data, self.idx)
        while self.len >0 and data > self.data[-1][0]:
            self.data.pop()
            self.len-=1
        
        self.data.append(pack)
        self.len+=1
        
        if self.data[0][1] < self.idx-self.max_size+1:
            self.data.popleft()
            self.len-=1
        self.idx +=1
    
    def get_max(self):
        return self.data[0][0]
    
def solution(stones, k):
    answer = 0
    stack = MaxStack(k)
    min_max = max(stones[0:k])
    for i, stone in enumerate(stones):
        stack.add(stone)
        if i>=k:
            min_max = min(min_max, stack.get_max())
        # print(stack.data, i)
    return min_max