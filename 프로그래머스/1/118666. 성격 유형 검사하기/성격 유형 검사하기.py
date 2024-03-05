def solution(survey, choices):
    answer = ''
    converter = {'A':'N', 'C':'F', 'M':'J', 'R':'T'}
    converter.update({v:k for k, v in converter.items()})
    data = {'A':0, 'N':0, 'C':0, 'F':0, 'M':0,'J':0, 'R':0,'T':0 }
    for i in range(len(survey)):
        sur, cho = survey[i], choices[i]
        print(sur[0],sur[1], cho, 8-cho)
        data[str(sur[0])] += 8-cho
        data[str(sur[1])] += cho
    
    if data['R']>=data['T']:
        answer+='R'
    else:
        answer+='T'
    if data['C']>=data['F']:
        answer+='C'
    else:
        answer+='F'
    if data['J']>=data['M']:
        answer+='J'
    else:
        answer+='M'
    if data['A']>=data['N']:
        answer+='A'
    else:
        answer+='N'
    
    print(data)
    return answer