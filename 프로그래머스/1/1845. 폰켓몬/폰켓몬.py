def solution(nums):
    answer = 0
    ponDict = {}
    ponDict = turnDict(nums)
    n = len(nums) //2
    answer = findPon(ponDict, n)
    return answer

# 순번:값 딕셔너리
def turnDict(nums):
    ponDict = {}
    for i in range(len(nums)):
        ponDict[i] = nums[i]
    return ponDict

def findPon(dict1, n):
    n_list = []
    for i in range(len(dict1)):
        if(dict1[i] not in n_list):
            n_list.append(dict1[i])
    if(len(n_list) >= n):
        return n
    for i in range(n):
        num = n - i
        if(len(n_list) == num):
            return num