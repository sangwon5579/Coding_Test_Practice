def solution(k, m, score):
    answer = 0
    times = len(score) // m
    score.sort(reverse=True)
    for i in range(times):
        answer += score[m-1 + (i*m)] * m
    return answer

