import math
def solution(n):
    answer = 0
    answer = check(n)
    return answer

def check(n):
    sqrt_num = int(math.sqrt(n))
    if(sqrt_num * sqrt_num == n):
        return (sqrt_num + 1) ** 2
    else:
        return -1