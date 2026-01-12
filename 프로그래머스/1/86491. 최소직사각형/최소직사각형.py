def solution(sizes):
    answer = 0
    leng = len(sizes)
    big_list = []
    small_list = []
    for i in range(len(sizes)):
        if(sizes[i][0] >= sizes[i][1]):
            big_list.append(sizes[i][0])
            small_list.append(sizes[i][1])
        else:
            big_list.append(sizes[i][1])
            small_list.append(sizes[i][0])
    big_list.sort(reverse = True)
    small_list.sort(reverse = True)
    answer = big_list[0] * small_list[0]
    return answer