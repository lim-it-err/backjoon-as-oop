def solution(friends, gifts):
    answer = 0
    user_idx = [0 for _ in range(len(friends))]
    idx_friend = {}
    gift_info = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    visited = [[False for _ in range(len(friends))] for _ in range(len(friends))]

    for i, friend in enumerate(friends):
        idx_friend[friend] = i
    for gift in gifts:
        src, dst = gift.split()
        gift_info[idx_friend[src]][idx_friend[dst]]+=1
        gift_info[idx_friend[dst]][idx_friend[src]]-=1
    
    for src in friends:
        for dst in friends:
            user_src, user_dst = idx_friend[src], idx_friend[dst]
            if user_src == user_dst:
                continue
            if visited[user_src][user_dst]:
                continue
            visited[user_src][user_dst], visited[user_dst][user_src] = True, True
            
            if gift_info[user_src][user_dst]>gift_info[user_dst][user_src]:
                user_idx[user_src]+=1
            elif gift_info[user_src][user_dst]<gift_info[user_dst][user_src]:
                user_idx[user_dst]+=1
            else:
                if sum(gift_info[user_src]) > sum(gift_info[user_dst]):
                    user_idx[user_src]+=1
                elif sum(gift_info[user_src]) < sum(gift_info[user_dst]):
                    user_idx[user_dst]+=1
    return max(user_idx)