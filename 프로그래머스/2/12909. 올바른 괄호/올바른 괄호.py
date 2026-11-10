def solution(s):
    answer = True
    n = len(s)
    list_s = list(s)
    k = 0
    for i in range(n):
        if(list_s[i] == "("):
            k += 1
        else:
            k -= 1
            if(k<0):
                answer = False
    if(k != 0):
        answer = False

    return answer