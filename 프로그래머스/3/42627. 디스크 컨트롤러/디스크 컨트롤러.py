def available_jobs(jobs, tic):
    #Pass Sorted available jobs
    available_jobs = []
    for job in jobs:
        if tic >= job[0]:
            available_jobs.append(job)
    available_jobs.sort(key=lambda x: x[1])
    return available_jobs

def solution(jobs):
    answer = 0
    N = len(jobs)
    jobs.sort()
    tic, next_tic = jobs[0][0], jobs[0][0]
    WORKING = False
    
    while len(jobs) or WORKING:
        if tic == next_tic:
            WORKING= False
            if not len(jobs):
                return answer // N
        current_available = available_jobs(jobs, tic)
        answer += len(current_available)
        if WORKING:
            answer += 1
        if not current_available or WORKING:
            tic += 1
            continue
        picked_job = current_available[0]
        jobs.remove(picked_job)
        next_tic = tic+ picked_job[1]
        tic += 1
        WORKING= True
    return answer // N