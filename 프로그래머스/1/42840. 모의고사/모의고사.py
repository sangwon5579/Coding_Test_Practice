def solution(answers):
    answer = []
    list1 = math1(len(answers))
    list2 = math2(len(answers))
    list3 = math3(len(answers))
    count1 = count(list1, answers)
    count2 = count(list2, answers)
    count3 = count(list3, answers)
    if(max(count1, count2, count3) == count1):
        answer.append(1)
    if(max(count1, count2, count3) == count2):
        answer.append(2)
    if(max(count1, count2, count3) == count3):
        answer.append(3)
    return answer


def math1(n):
    n_list = []
    for i in range(n):
        k = i % 5 + 1
        n_list.append(k)
    return n_list
        
def math2(n):
    t_list = [2,1,2,3,2,4,2,5]
    n_list = []
    for i in range(n):
        k = i%8
        n_list.append(t_list[k])
    return n_list

def math3(n):
    t_list = [3,3,1,1,2,2,4,4,5,5]
    n_list = []
    for i in range(n):
        k = i%10
        n_list.append(t_list[k])
    return n_list
        
def count(n_list, answer):
    count = 0
    for i in range(len(n_list)):
        if(n_list[i] == answer[i]):
            count += 1
    return count