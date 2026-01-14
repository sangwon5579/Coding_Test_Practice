def solution(number, limit, power):
    answer = 0
    for i in range(number):
        answer += limitNum(findNumDivisor(i+1), limit, power)
    
    return answer

import math
# 약수 개수
def findNumDivisor(num):
    if(num == 1):
        return 1
    count = 0
    number = int(math.sqrt(num))
    for i in range(number):
        n = i+1
        if (num % n == 0):
            count += 1
            if(n * n != num):
                count += 1
            
            
    return count



# 리미트 검증
def limitNum(num, limit, power):
    if(num > limit):
        return power
    else:
        return num