def solution(n, arr1, arr2):
    answer = []
    arr1Bin = toBin(arr1, n)
    arr2Bin = toBin(arr2, n)
    reArr = sumArr(arr1Bin, arr2Bin, n)
    answer = outAns(reArr, n)
    return answer


# 이진수 배열로 
def toBin(arr, n):
    binArr = []
    for i in range(len(arr)):
        binArr.append(format(arr[i], 'b').zfill(n))
    return binArr

# 지도 병합
def sumArr(arr1, arr2, n):
    listArr1 = listArr(arr1, n)
    listArr2 = listArr(arr2, n)
    sumArra = sumList(listArr1, listArr2, n)
    reArray = reArr(sumArra, n)
    return reArray
    
# 각 자리수 리스트로
def listArr(arr, n):
    returnArr = []
    for i in range(n):
        returnArr += list(arr[i])
    return returnArr

def sumList(arr1, arr2, n):
    sumArr = []
    for i in range(len(arr1)):
        sumArr.append(sumBin(arr1[i], arr2[i]))
    return sumArr

def sumBin(a, b):
    if((a == '0' and b == '0') or (a == 0 and b == 0)):
        return 0
    else:
        return 1
    
def reArr(arr, n):
    returnArr = []
    for i in range(n):
        returnArr.append(arr[i*n:(i+1)*n])
    return returnArr

def outAns(arr, n):
    answer = []
    for i in range(n):
        answer.append(change(arr[i], n))
    return answer
        
# #, " " 으로
def change(arr, n):
    answer = ""
    for i in range(n):
        answer += changeIn(arr[i])
    return answer

def changeIn(a):
    if(a == 1 or a == '1'):
        return "#"
    else:
        return " "
    
# 한변 길이 n
# 공백 " " or  벽 "#"
# 지도1 + 지도2
# 공백 and, 벽 or
# 정수 배열로 암호화
# 벽부분 1, 공백 부분 0 
