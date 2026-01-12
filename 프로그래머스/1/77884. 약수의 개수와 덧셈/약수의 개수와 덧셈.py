def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if find_divisor(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

def find_divisor(num):
    count = 0
    for i in range(num):
        if num %(i+1) == 0:
            count += 1
    return count


