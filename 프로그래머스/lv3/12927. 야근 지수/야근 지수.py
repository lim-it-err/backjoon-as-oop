def solution(n, works):
    works.sort(reverse=True)  # 작업량을 내림차순으로 정렬합니다.

    while n > 0:
        max_work = works[0]  # 가장 큰 작업량을 가진 일을 선택합니다.

        if max_work == 0:  # 모든 작업량이 0이면 종료합니다.
            break

        for i in range(len(works)):
            if works[i] < max_work:  # 가장 큰 작업량과 같은 작업량을 갖는 일을 찾습니다.
                break
            works[i] -= 1  # 해당 작업량을 1씩 감소시킵니다.
            n -= 1  # 남은 시간을 1씩 감소시킵니다.

            if n == 0:  # 남은 시간이 0이면 종료합니다.
                break

    return sum(work**2 for work in works)  # 각 일의 작업량을 제곱하여 더한 값을 반환합니다.
