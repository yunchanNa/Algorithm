def solution(new_id):
    answer = ''
    a = []
    allow = ['-','_','.']
    answer = list(new_id.lower())
    for i in answer:
        if i.isalpha() == True or i.isnumeric() == True or i in allow:
            a.append(i)
        else:
            continue
    answer = ''.join(a)
    while answer.find('..') != -1:
        answer = answer.replace('..','.')
    a = list(answer)
    if a[0] == '.':
        a.pop(0)
    if len(a) != 0:
        if a[-1] == '.':
            a.pop(-1)
    if len(a) == 0:
        a.append('a')
    if len(a) >= 16:
        a = a[0:15]
        if a[-1] == '.':
            a = a[0:14]
    if len(a) <= 2:
        while len(a) < 3:
            a.append(a[-1])
    answer = ''.join(a)
    return answer
