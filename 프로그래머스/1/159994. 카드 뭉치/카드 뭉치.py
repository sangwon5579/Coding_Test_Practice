def solution(cards1, cards2, goal):
    answer = ''
    c1 = len(cards1)
    c2 = len(cards2)
    g = len(goal)
    # if c1 + c2 != g:
    #     answer = "No"
    #     return answer
    num1 = 0
    num2 = 0
    for i in range(g):
        if(num1 < c1 and goal[i] == cards1[num1]):
            num1+=1
        elif(num2 < c2 and goal[i] == cards2[num2]):
            num2 += 1
        else:
            answer = "No"
            return answer

    if answer != "No":
        answer = "Yes"
    return answer  