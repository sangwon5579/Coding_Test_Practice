def solution(s):
    answer = 0
    s_list = list(s)
    if(s_list[0] == "+"):
        for i in range(len(s) - 1):
            answer = answer *10 + int(s_list[i+1])
    elif(s_list[0] == "-"):
        for i in range(len(s) - 1):
            answer = answer * 10 + int(s_list[i+1])
        answer = -answer
    else:
        answer = int(s)
    return answer