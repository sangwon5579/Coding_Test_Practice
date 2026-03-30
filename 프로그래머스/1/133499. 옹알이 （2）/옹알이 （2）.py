def solution(babbling):
    answer = 0
    sounds = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        prev =""
        valid = True
        j = 0
        
        while(j < len(babbling[i])):
            matched = False
            
            for s in sounds:
                if babbling[i].startswith(s, j) and prev != s:
                    j += len(s)
                    prev = s
                    matched = True
                    break
                    
            if not matched:
                valid=False
                break
        if valid:
            answer += 1
    return answer


# aya ye woo ma