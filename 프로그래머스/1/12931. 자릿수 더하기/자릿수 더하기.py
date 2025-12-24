def solution(n):
    answer = 0
    n_list = []
    leng = len(str(n))
    for i in range(leng):
        a = 10 ** (leng - i -1)
        num = n // a % 10
        n_list.append(num)
        
    for j in range(len(n_list)):
        answer += n_list[j]
    

    return answer