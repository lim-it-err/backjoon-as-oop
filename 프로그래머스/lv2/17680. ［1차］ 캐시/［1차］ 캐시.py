class Cache():
    def __init__(self, size=1):
        self.max_size = size
        self.queue = []
        self.is_key = set()
        self.current_size = 0
        self.idx = 0
        
    def push(self, data: str):
        time_cost = 0
        if data in self.is_key:
            time_cost = 1
            self.queue.remove(data)
        else:
            time_cost = 5
            self.is_key.add(data)
        self.queue.append(data)
        if self._is_full():
            self.pop(policy="lru")
        return time_cost
        
    def pop(self, policy="lru"):
        if policy == "lru":
            least_recent = self.queue[0]
            self.is_key.remove(least_recent)
            self.queue = self.queue[1:]
        self.current_size -=1
        return least_recent

        
    def _is_full(self):
        return len(self.queue) == self.max_size + 1
    
    
def solution(cacheSize, cities):
    cache = Cache(size=cacheSize)
    total_time = 0
    for city in cities:
        city = city.lower()
        total_time+=cache.push(city)
    return total_time