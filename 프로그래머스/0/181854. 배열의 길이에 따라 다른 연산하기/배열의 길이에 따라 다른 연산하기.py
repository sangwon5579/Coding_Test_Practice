def solution(arr, n):
    answer = []
    a = len(arr)
    if a % 2 != 0:
        for i in range(a):
            if i % 2 == 0:
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
    else:
        for i in range(a):
            if i % 2 == 0:
                answer.append(arr[i])
            else:
                answer.append(arr[i] + n)
    return answer