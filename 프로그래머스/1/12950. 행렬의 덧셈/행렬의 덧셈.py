def solution(arr1, arr2):
    answer = []
    len_out = len(arr1)
    if(len_out == 0):
        len_in = 0
    else:
        len_in = len(arr1[0])
    for i in range(len_out):
        row = []
        for j in range(len_in):
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)
    return answer