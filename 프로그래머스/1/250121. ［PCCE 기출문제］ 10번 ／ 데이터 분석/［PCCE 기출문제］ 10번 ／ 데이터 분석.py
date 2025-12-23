def solution(data, ext, val_ext, sort_by):
    answer = []
    answer = find_ext(answer, data, ext, val_ext)
    answer = sort_data(answer, sort_by)
    return answer

def find_ext(answer, data, ext, val_ext):
    if ext == "code":
        num = 0
    elif ext == "date":
        num = 1
    elif ext == "maximum":
        num = 2
    else:
        num = 3
    d = len(data)
    for i in range(d):
        if(data[i][num] < val_ext):
            answer.append(data[i])
    return answer

def sort_data(answer, sort_by):
    if(sort_by == "code"):
        num = 0
    elif(sort_by == "date"):
        num = 1
    elif(sort_by == "maximum"):
        num = 2
    else:
        num = 3
    answer.sort(key=lambda x: x[num])
    return answer

# code / date / maximum / remain
# ext sort_by = code, date, maximum, remain
# data에서 ext 값이 val_ext보다 작은 데이터 추출
# sort_by에 해당값 기준 오름차순 정렬