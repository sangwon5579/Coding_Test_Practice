def solution(players, callings):
    answer = []
    dicta = {name: i
           for i, name in enumerate(players)}
    call_times =len(callings)
    for i in range(call_times):
        a = dicta[callings[i]]
        b = players[a-1] 
        dump = players[a] 
        players[a] = players[a-1] 
        players[a-1] = dump
        dicta[callings[i]] -= 1
        dicta[b] += 1
    answer = players
    return answer

