import heapq
def parse(operation):
    instruction, detail = operation.split(' ')
    return instruction, int(detail)
    

def solution(operations):
    heap = []
    heap2 = []
    answer = []
    counter = 0
    
    for operation in operations:
        instruction, num = parse(operation)
        if counter == 0:
            heap = []
            heap2 = []
        if instruction == "I":
            heapq.heappush(heap, num)
            heapq.heappush(heap2, -num)
            counter+=1
        elif instruction == "D" and num == 1:
            if len(heap2)!=0:
                heapq.heappop(heap2)
                counter = max(0, counter-1)
        elif instruction == "D" and num == -1:
            if len(heap)!=0:
                heapq.heappop(heap)
                counter = max(0, counter-1)
    if not counter:
        return [0,0]
    return [heapq.heappop(heap2)*-1, heapq.heappop(heap)]