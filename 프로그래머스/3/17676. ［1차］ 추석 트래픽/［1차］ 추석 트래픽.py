def get_start(h, m, s, mm, response_t):
    n_mm = (s*1000+mm - response_t)%1000
    n_s =int((s*1000+mm - response_t)//1000)%60
    if n_s > s:
        n_m = (m-1)%60
    else:
        n_m = m
    if n_m > m:
        n_h = h-1
    else:
        n_h = h
    return (n_h, n_m, n_s, int(n_mm))
def parse(line):
    _, finish_t, response_t = line.split()
    response_t = int(float(response_t[:-1])*1000)
    h, m, s = finish_t.split(':')
    s, mm = s.split('.')
    h, m, s= map(int, [h, m, s])
    mm = float(mm)
    
    return get_start(h, m, s, mm, response_t-1), (h, m, s, int(mm))
    
def hashing(t):
    a,b,c,d = t
    return (((a+1)*60+b)*60+c)*1000+d
def solution(lines):
    answer = 0
    v = {}
    for line in lines:
        s_t, e_t = parse(line)
        for i in range(hashing(s_t)-1000, hashing(e_t)):
            try:
                v[i]+=1
            except KeyError:
                v[i] = 1
    return max(list(v.values()))