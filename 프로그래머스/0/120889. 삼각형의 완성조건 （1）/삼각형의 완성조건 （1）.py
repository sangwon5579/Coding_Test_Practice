def solution(sides):
    answer = 0
    sides.sort()
    answer = check(sides)
    return answer

def check(sides):
    if(sides[2] < sides[0] + sides[1]):
        return 1
    else:
        return 2