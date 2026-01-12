def solution(x):
    answer = True
    h_list = list(map(int, str(x)))
    h = 0
    for i in range(len(h_list)):
        h += h_list[i]
    if (x % h == 0):
        answer = True
    else:
        answer = False
    return answer