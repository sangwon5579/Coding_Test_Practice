def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1):
        if(yellow%i == 0 and i>= yellow/i):
            k = 2*(i + yellow/i) + 4
            if(k == brown):
                answer = [i+2, yellow/i+2]
                break
    return answer