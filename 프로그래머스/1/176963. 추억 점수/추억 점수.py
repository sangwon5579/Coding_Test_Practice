def solution(name, yearning, photo):
    answer = []
    point_dict = dict()
    for i in range(len(name)):
        point_dict[name[i]] = yearning[i]
    
    for k in range(len(photo)):
        point = 0
        for j in range(len(photo[k])):
            if(photo[k][j] in point_dict):
                point += int(point_dict[photo[k][j]])
            else:
                point += 0
        answer.append(point)
    return answer