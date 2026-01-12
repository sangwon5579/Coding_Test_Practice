def solution(s):
    answer = ''
    j = 0
    for i in range(len(s)):
        
        if(s[i] == " "):
            j = 0
            answer += " "
        elif (j == 0 or j % 2 == 0):
            answer += (s[i].upper())
            j+=1
        else:
            answer += (s[i].lower())
            j+=1
        
    return answer