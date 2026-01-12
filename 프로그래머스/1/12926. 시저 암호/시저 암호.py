def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if(s[i] == " "):
            answer += " "
        else:
            if('a' <= s[i] <= 'z'):
                if(ord(s[i])+n > ord('z')):
                    answer += chr(ord('a') + n  + ord(s[i]) - ord('z') - 1)
                else:
                    answer += chr(ord(s[i]) + n)
            else:
                if(ord(s[i])+n > ord('Z')):
                    answer += chr(ord('A') + n  + ord(s[i]) - ord('Z') - 1)
                else:
                    answer += chr(ord(s[i]) + n)
            
    return answer

# ord 문자 -> 아스키
# chr 아스키 -> 문자