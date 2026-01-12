def solution(n, m):
    answer = []
    answer.append(gcd(n, m))
    answer.append(lcm(n, m))
    return answer

# Greatest Common Divisor 최대공약수
def gcd(n, m):
    n_list = []
    for i in range(n):
        if(n%(i+1) == 0 and m%(i+1) == 0):
            n_list.append(i+1)
    n_list.sort(reverse=True)
    return n_list[0]
    
# Least Common Multiple 최소공배수
def lcm(n, m):
    n_list = []
    m_list = []
    a_list = []
    for i in range(m):
        n_list.append((i+1) * n)
    for j in range(n):
        m_list.append((j+1) * m)
    for k in range(m):
        if(n_list[k] in m_list):
            a_list.append(n_list[k])
    a_list.sort()
    return a_list[0]