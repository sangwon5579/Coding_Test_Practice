def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    def dfs(cur):
        visited[cur] = True
        for i in range(n):
            if computers[i][cur] == 1 and not visited[i]:
                dfs(i)
    
    for j in range(n):
        if not visited[j]:
            answer+=1
            dfs(j)
    return answer