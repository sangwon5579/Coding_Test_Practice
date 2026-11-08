def solution(sizes):
    answer = 0
    n = len(sizes)
    for i in range(n):
        sizes[i] = sorting(sizes[i])
    a = 0
    b = 0
    for i in range(n):
        if(a < sizes[i][0]):
            a = sizes[i][0]
        if(b < sizes[i][1]):
            b = sizes[i][1]
    answer = a * b
    return answer

def sorting(a):
    if(a[0] < a[1]):
        tmp = a[0]
        a[0] = a[1]
        a[1] = tmp
    return a
