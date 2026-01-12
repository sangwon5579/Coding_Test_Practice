def solution(s):
    answer = []
    for i in range(len(s)):
        n_list = []
        for j in range(len(s)):
            if(s[i] == s[j] and i != j and i > j):
                n_list.append(j)
        if(len(n_list) == 0):
            answer.append(-1)
        else:
            n_list.sort(reverse = True)
            answer.append(i - n_list[0])
        
    return answer