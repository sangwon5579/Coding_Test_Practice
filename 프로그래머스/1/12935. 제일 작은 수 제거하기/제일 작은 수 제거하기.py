def solution(arr):
    answer = []
    small_list = sorted(arr)
    arr.remove(small_list[0])
    if len(arr) == 0:
        answer.append(-1)
    else:
        answer = arr
    return answer