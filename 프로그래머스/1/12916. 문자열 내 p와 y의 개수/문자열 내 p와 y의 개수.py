def solution(s):
    answer = True
    s_list = list(s)
    num_p = 0
    num_y = 0
    for i in range(len(s_list)):
        if(s_list[i] == "p" or s_list[i] == "P"):
            num_p += 1
        elif(s_list[i] == "y" or s_list[i] == "Y"):
            num_y += 1
    if(num_p == num_y):
        return True
    else:
        return False