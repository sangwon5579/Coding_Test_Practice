def solution(s):   
    answer = ''
    n_list = s.split()
    int_list = []
    for i in range(len(n_list)):
        int_list.append(int(n_list[i]))
    a = max(int_list)
    b = min(int_list)
    answer = str(b) + " " + str(a)
    return answer