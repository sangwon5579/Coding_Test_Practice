def solution(n):
    answer = 0
    th_list = []
    share = n
    t = True
    while(t == True):
        if(share < 3):
            th_list.append(share)
            t = False
        else:
            th_list.append(share % 3)
            share = share // 3
    for i in range(len(th_list)):
        n = len(th_list) - 1 - i
        answer += th_list[i] * (3 ** n)
    return answer
