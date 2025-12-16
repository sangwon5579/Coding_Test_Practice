def solution(t, p):
    answer = 0
    p_len = len(p)
    t_list = list(map(int, t))
    num_list =[]
    t_len = len(t)
    count = t_len - p_len + 1
    for i in range(count):
        sub_num = []
        for j in range(p_len):
            sub_num.append(t_list[i+j])
        sub = int("".join(map(str, sub_num)))
        num_list.append(sub)
    total_count = 0
    for i in range(len(num_list)):
        if int(num_list[i]) <= int(p):
            total_count += 1
    answer = total_count
    return answer

