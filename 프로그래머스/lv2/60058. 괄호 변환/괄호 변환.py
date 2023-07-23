def divide(input_str):
    cnt = 0
    i = 0
    for i in range(len(input_str)):
        if input_str[i] == "(":
            cnt+=1
        else:
            cnt-=1
        if cnt == 0:
            break
    return input_str[:i+1], input_str[i+1:]
def is_appropriate(input_str):
    cnt = 0
    for i in range(len(input_str)):
        if input_str[i] == "(":
            cnt+=1
        else:
            cnt-=1
        if cnt <0:
            return False
    return True
        
def solution(p):
    answer = ''

    while True:
        if not p:
            return answer
        u, v = divide(p)
        if is_appropriate(u):
            p = v
            answer += u
            continue
        else:
            _u = u[1:-1]
            print(_u)
            __u = ""
            for i in range(len(_u)):
                if _u:
                    if _u[i] == "(":
                        __u+=")"
                    else:
                        __u+="("
                        # TypeError: 'str' object does not support item assignment
            answer += "("
            answer += solution(v)
            answer += ")"
            answer += __u
            break
            
    return answer