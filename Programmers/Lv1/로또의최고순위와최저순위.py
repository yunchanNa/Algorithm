Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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