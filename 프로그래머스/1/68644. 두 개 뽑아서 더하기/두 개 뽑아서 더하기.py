def solution(numbers):
    answer = []
    leng = len(numbers)
    for i in range(leng):
        for j in range(leng):
            k = 0
            if(i != j):
                k = numbers[i] + numbers[j]
                if k not in answer:
                    answer.append(k)
    answer.sort()
    return answer