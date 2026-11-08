def solution(answers):
    answer = []
    list1 = [1,2,3,4,5]
    list2 = [2,1,2,3,2,4,2,5]
    list3 = [3,3,1,1,2,2,4,4,5,5]
    a = 0;
    b = 0;
    c = 0;
    n = len(answers)
    for i in range(n):
        if(answers[i] == list1[i%5]):
            a += 1
        if(answers[i] == list2[i%8]):
            b+=1
        if(answers[i] == list3[i%10]):
            c+=1
    m = max(a, b, c)
    if(m==a):
        answer.append(1)
    if(m==b):
        answer.append(2)
    if(m==c):
        answer.append(3)
    return answer