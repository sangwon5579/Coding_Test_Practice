def solution(wallet, bill):
    answer = 0
    
    if(wallet[0] > wallet[1]):
        w_small = wallet[1]
        w_big = wallet[0]
    else:
        w_small = wallet[0]
        w_big = wallet[1]
        
    if(bill[0] > bill[1]):
        b_small = bill[1]
        b_big = bill[0]
    else:
        b_small = bill[0]
        b_big = bill[1]
        
    while(b_small > w_small or b_big > w_big):
        if(bill[0] > bill[1]):
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        answer += 1
        
        if(bill[0] > bill[1]):
            b_small = bill[1]
            b_big = bill[0]
        else:
            b_small = bill[0]
            b_big = bill[1]
    return answer

