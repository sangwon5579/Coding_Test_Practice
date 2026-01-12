def solution(number):
    answer = 0
    leng = len(number)
    for i in range(leng):
        for j in range(leng):
            for k in range(leng):
                if(i != j and j != k and i != k):
                    if(number[i] + number[j] + number[k] == 0):
                        answer += 1
    answer = answer // 6
    return answer