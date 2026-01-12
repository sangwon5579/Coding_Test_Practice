def solution(a, b):
    answer = 0
    if(a == b):
        answer = a
    elif(a > b):
        answer = check(b, a)
    else:
        answer = check(a, b)
    return answer

def check(small, big):
    answer = 0
    for i in range(small, big+1, 1):
        answer += i
    return answer