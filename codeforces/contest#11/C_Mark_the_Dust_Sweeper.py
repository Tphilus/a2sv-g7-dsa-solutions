import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dust = list(map(int, input().split()))
    
    start = 0
    while start < n and dust[start] == 0:
        start += 1
    
    totalOperations = 0
    for i in range(start,  n - 1):
        if dust[i] == 0:
            totalOperations += 1
        else:
            totalOperations += dust[i]
    
    print(totalOperations)