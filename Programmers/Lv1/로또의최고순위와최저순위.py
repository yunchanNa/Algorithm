def solution(lottos, win_nums):
    answer = []
    rank = [6,6,5,4,3,2,1]
    cnt = lottos.count(0)
    ans = 0
    for i in win_nums:
        if i in lottos:
            ans += 1
    answer.append(rank[cnt + ans])
    answer.append(rank[ans])
    return answer
