def solution(n):
    answer = 0
    answer = findPrime(n)
    return answer



def findPrime(num):
    count = 0
    num_list= [0] * (num+1)
    for i in range(2, num+1):
        num_list[i] = i
    for i in range(2, num+1):
        if(num_list[i] == 0):
            continue
        for j in range(2*i, num+1, i):
            num_list[j] = 0
    for i in range(2, num+1):
        if(num_list[i] != 0):
            count += 1
    return count
    
    
