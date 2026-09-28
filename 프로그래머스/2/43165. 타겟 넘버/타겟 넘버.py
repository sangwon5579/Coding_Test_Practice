def solution(numbers, target):
    answer = 0
    def dfs(index, total):
        if(index == len(numbers)):
            if(total == target):
                return 1
            else:
                return 0
        
        plus = dfs(index+1, total+numbers[index])
        minus = dfs(index+1, total-numbers[index])
        return plus + minus
    answer = dfs(0,0)
    return answer
