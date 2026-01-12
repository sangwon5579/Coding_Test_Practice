def solution(phone_number):
    answer = ''
    leng = len(phone_number)
    phone_list = list(phone_number)
    digit = 0
    answer_list = []
    while(leng > 4):
        answer_list += "*"
        digit += 1
        leng -= 1
    for j in range(4):
        answer_list += phone_list[digit]
        digit += 1
    for k in range(len(phone_list)):
        answer += answer_list[k]
    return answer