def solution(n):
    answer = 0
    n2 = bin(n)[2:]
    for i in range(20):
        num = bin(n+i+1)[2:]
        if(countOne(n2) == countOne(num)):
            answer = n+i+1
            break
    return answer

def countOne(n):
    count = 0
    for i in range(len(n)):
        if(n[i] == '1'):
            count += 1
    return count 