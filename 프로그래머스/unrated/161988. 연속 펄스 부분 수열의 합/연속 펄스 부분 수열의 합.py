def solution(sequence):
    def set_pulse_array(_lst, start_with=-1):
        N = len(_lst)
        ret_arr = [0 for i in range(N)]
        pulse = [-start_with if i%2 else start_with for i in range(N)]
        for i in range(N):
            ret_arr[i] = _lst[i]*pulse[i]
        return ret_arr
            

    def get_maxsum_in_sublist(_lst):
        lst_length = len(_lst)
        
        submax_list = [0 for i in range(lst_length)]
        for i in range(lst_length):
            if i == 0:
                submax_list[i] = _lst[i]
            else:
                submax_list[i] = max(_lst[i], submax_list[i-1]+_lst[i])
        return max(submax_list)
    return max(get_maxsum_in_sublist(set_pulse_array(sequence, 1)), get_maxsum_in_sublist(set_pulse_array(sequence, -1)))
