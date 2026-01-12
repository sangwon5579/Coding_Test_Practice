def solution(s):
    answer = True
    # s_list = list(s)
    # for i in range(len(s)):
    #     if(s_list[i].isdigit()):
    #         answer = True
    #     else:
    #         answer = False
    #         return answer
    if(s.isdigit() and (len(s) == 4 or len(s) == 6)):
        answer = True
    else:
        answer = False
    return answer