def solution(strings, n):
    answer = []
    
    data = tuple(
        list(i) for i in strings
                )
    sort_data = sorted(data, key=lambda x:(x[n], x))
    
    for i in range(len(sort_data)):
        a = "".join(sort_data[i])
        answer.append(a)
    return answer