from collections import defaultdict
def solution(edges):
    answer = [0,0, 0, 0]
    edges_outbound = defaultdict(list)
    edges_inbound = defaultdict(list)
    for edge in edges:
        src, dst = edge
        edges_outbound[src].append(dst)
        edges_inbound[dst].append(src)
    max_idx, max_len = 0, 0
    for key in edges_outbound.keys():
        if max_len < len(edges_outbound[key]):
            max_len = len(edges_outbound[key])
            max_idx = key
    answer[0] = max_idx
    for key in edges_inbound.keys():
        if not edges_outbound[key]:
            answer[2] +=1
            continue
        if key == max_idx:
            continue
        elif len(edges_outbound[key]) == 2 and len(edges_inbound[key]) >= 2:
            answer[3] += 1
    answer[1] = max_len-answer[2]-answer[3]
    return answer