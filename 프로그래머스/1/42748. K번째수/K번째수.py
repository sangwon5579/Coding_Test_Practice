def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        n_list =[]
        for j in range(commands[i][0]-1, commands[i][1]):
            n_list.append(array[j])
        n_list.sort()
        n = commands[i][2] - 1
        answer.append(n_list[n])
    return answer