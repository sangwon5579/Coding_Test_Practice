def solution(s):
    answer = ''
    leng = len(s)
    if(leng % 2 == 0):
        answer = even(s, leng)
    else:
        answer = odd(s, leng)
    return answer

def even(s, leng):
    leng = leng /2 -1
    leng = int(leng)
    answer = s[leng] + s[leng+1]
    return answer

def odd(s, leng):
    leng = (leng-1) / 2
    leng = int(leng)
    answer = s[leng]
    return answer