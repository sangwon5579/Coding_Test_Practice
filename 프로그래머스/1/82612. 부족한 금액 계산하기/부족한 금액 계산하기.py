def solution(price, money, count):
    answer = -1
    total = 0
    for i in range(count):
        total += price * (i+1)
    if(money >= total):
        answer = 0
    else:
        answer = total - money
    return answer