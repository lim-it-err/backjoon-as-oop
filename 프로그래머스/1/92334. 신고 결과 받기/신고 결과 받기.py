from collections import defaultdict
def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report_arr = [[False for _ in range(len(id_list))] for _ in range(len(id_list))]
    reporter = defaultdict(list)
    idx_user = {}
    for i, user in enumerate(id_list):
        idx_user[user] = i
    for repo in report:
        src, dst = repo.split()
        report_arr[idx_user[dst]][idx_user[src]] = True
        reporter[idx_user[dst]].append(idx_user[src])
        reporter[idx_user[dst]] = list(set(reporter[idx_user[dst]]))
    for user in id_list:
        if sum(report_arr[idx_user[user]]) >= k:
            for single_reporter in reporter[idx_user[user]]:
                answer[single_reporter]+=1
    return answer