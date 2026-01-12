def solution(n):
    answer = 0
    n_list = list(map(int, str(n)))
    n_list.sort(reverse = True)
    for i in range(len(n_list)):
                  answer = answer * 10 + int(n_list[i])
    return answer