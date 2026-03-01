from itertools import combinations

def solution(nums):
    answer = 0
    for c in combinations(nums, 3):
        answer += isPrime(c[0] + c[1] + c[2])

    return answer

def isPrime(n):
    answer = 0
    for i in range(2, n-1):
        if(n % i == 0):
            answer += 1
        else:
            answer += 0
    if(answer == 0):
        return 1
    else:
        return 0