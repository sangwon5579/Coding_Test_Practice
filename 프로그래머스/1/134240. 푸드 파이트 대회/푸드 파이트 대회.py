def solution(food):
    answer = ''
    leng = len(food) - 1
    for i in range(leng):
        n = food[i+1] // 2
        for j in range(n):
            answer += str(i+1)
    reanswer = answer[::-1]
    answer = str(answer) + str(0) + str(reanswer)
    return answer