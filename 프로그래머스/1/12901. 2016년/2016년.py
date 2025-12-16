def solution(a, b):
    answer = ''
    answer = define(a, b)
    return answer

def define(a, b):
    num = 1
    if a == 1:
        num = b
    elif a == 2:
        num = 31 + b
    elif a == 3:
        num = 60 + b
    elif a == 4:
        num = 91 + b
    elif a == 5:
        num = 121 + b
    elif a == 6:
        num = 152 + b
    elif a == 7:
        num = 182 + b
    elif a == 8:
        num = 213 + b
    elif a == 9:
        num = 244 + b
    elif a == 10:
        num = 274 + b
    elif a == 11:
        num = 305 + b
    else:
        num = 335 + b
    num = num % 7
    if num == 0:
        answer = "THU"
    elif num == 1:
        answer = "FRI"
    elif num == 2:
        answer = "SAT"
    elif num == 3:
        answer = "SUN"
    elif num == 4:
        answer = "MON"
    elif num == 5:
        answer = "TUE"
    elif num == 6:
        answer = "WED"
    return answer