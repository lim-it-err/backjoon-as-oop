from collections import deque, defaultdict
import copy
def preprocess(tickets):
    ticket_dict = defaultdict(list)
    for ticket in tickets:
        src, dst = ticket
        ticket_dict[src].append(dst)
    return ticket_dict

def solution(tickets):
    answer = []
    route_list = [["ICN"]]
    ticket_dict = preprocess(tickets)    

    sta = deque()
    sta.append((["ICN"], ticket_dict))
    while sta:
        route, remain_ticket = sta.popleft()
        if len(route) == len(tickets)+1:
            answer.append(route)
            continue
        for dst in remain_ticket[route[-1]]:
            new_route = route[:]+[dst]
            remain_ticket_copy = copy.deepcopy(remain_ticket)
            remain_ticket_copy[route[-1]].remove(dst)
            sta.append((new_route, remain_ticket_copy))
        
    answer.sort()
    return answer[0]