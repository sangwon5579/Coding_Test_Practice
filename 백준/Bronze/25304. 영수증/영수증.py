total = int(input())
n = int(input())
total_hap = 0
for _ in range(n):
    t = input()
    a, b = t.split()
    a = int(a)
    b = int(b)
    hap = a*b
    total_hap += hap
if(total == total_hap):
    print('Yes')
else:
    print('No')