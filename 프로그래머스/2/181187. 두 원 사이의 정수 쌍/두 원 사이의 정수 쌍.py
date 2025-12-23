def solution(r1, r2):
    import math
    answer = 0
    a = 1
    b = r2 + 1
    rr2 = r2 * r2
    rr1 = r1 * r1

    for i in range(a,b):
        if(i < r1):
            min_y = int(math.ceil(math.sqrt(r1*r1 - i*i)))
        else:
            min_y = 0
        max_y = int(math.sqrt(r2*r2 - i*i))
        answer += max_y - min_y + 1
    answer = answer * 4
    # dot = r2 - r1 + 1
    # answer += (dot * 4)
    return answer
