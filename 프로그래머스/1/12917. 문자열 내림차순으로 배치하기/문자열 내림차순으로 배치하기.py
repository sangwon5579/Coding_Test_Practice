def solution(s):
    answer = ''
    s_list = list(s)
    s_list.sort(reverse=True)
    for i in range(len(s_list)):
        answer += s_list[i]
    return answer