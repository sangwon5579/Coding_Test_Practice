def solution(A,B):
    answer = 0
    list_a = sorted(A)
    list_b = sorted(B)
    for i in range(len(A)):
        answer += list_a[i] * list_b[len(A) - i-1]

    return answer