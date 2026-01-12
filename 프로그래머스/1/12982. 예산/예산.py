def solution(d, budget):
    answer = 0
    total = 0
    d.sort()
    for i in range(len(d)):
        if(total + d[i] > budget):
            return answer
        else:
            total += d[i]
            answer += 1
    return answer