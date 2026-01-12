def solution(absolutes, signs):
    answer = 0
    leng = len(absolutes)
    answer = calcu(absolutes, signs, leng)
    return answer

def calcu(num, boo, leng):
    answer = 0
    for i in range(leng):
        if(boo[i] == True):
            answer += num[i]
        else:
            answer -= num[i]
    return answer