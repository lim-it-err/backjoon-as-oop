def solution(cap, n, deliveries, pickups):
    answer = 0
    acc_del = [-1 for _ in range(len(deliveries))]
    acc_pic = [-1 for _ in range(len(pickups))]
    acc_del[-1] = deliveries[-1]
    acc_pic[-1] = pickups[-1]
    
    for i in range(len(acc_del)-1, -1, -1): 
        if i == len(acc_del)-1:
            continue
        acc_del[i] = acc_del[i+1]+deliveries[i]
    for i in range(len(acc_pic)-1, -1, -1): 
        if i == len(acc_pic)-1:
            continue
        acc_pic[i] = acc_pic[i+1]+pickups[i]

    num_car = 0
    for i in range(len(acc_pic)-1, -1, -1):
        needs_car_idx= max(acc_pic[i], acc_del[i])
        if needs_car_idx>num_car*cap:
            _num_car = needs_car_idx //cap + int(bool(needs_car_idx%cap))
            answer += (i+1)*(_num_car-num_car)*2
            num_car = _num_car
    return answer