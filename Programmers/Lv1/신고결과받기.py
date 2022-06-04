import os
from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    count = defaultdict(int)
    user = defaultdict(list)
    for r in report:
        a,b = r.split()
        if b not in user[a]:
            user[a].add(b)
            count[b] += 1
    for id in id_list:
        result = 0
        for u in user[id]:
            if count[u] >= k:
                result += 1
        answer.append(result)
    return answer
os.system('pause')
