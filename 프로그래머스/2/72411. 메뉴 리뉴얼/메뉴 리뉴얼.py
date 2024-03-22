from collections import defaultdict, OrderedDict
def add_sub(dic,  order, num, cnt):
    if order is None:
        return
    if cnt == num:
        dic[order] =1
        return
    for i in range(len(order)):
        add_sub(dic, order[0:i]+order[i+1:], num, cnt-1)
    
def solution(orders, course):
    answer = []
    for i, order in enumerate(orders):
        order = list(order)
        order.sort()
        orders[i] = ["".join(order)][0]
    
    for number in course:
        substring = OrderedDict()            
        max_value = -1

        for order in orders:

            tmp_dict = defaultdict(int)
            add_sub(tmp_dict, order, number, len(order))
            for key in tmp_dict:
                if key in substring:
                    substring[key]+=1
                else:
                    substring[key] = 1
                max_value = max(max_value, substring[key])
        for key in substring:
            if substring[key]>1 and substring[key] == max_value:
                answer.append(key)
    answer.sort()
    return answer