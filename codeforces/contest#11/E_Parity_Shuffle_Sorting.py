import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        return

    ops = []

    ops.append((1, n))
    if (a[0] + a[n - 1]) % 2 == 1:
        x = a[0]
    else:
        x = a[n - 1]

    for i in range(2, n):  
        if (x + a[i - 1]) % 2 == 1:
            ops.append((1, i))   
        else:
            ops.append((i, n))  

    print(len(ops))
    for l, r in ops:
        print(l, r)

t = int(input())
for _ in range(t):
    solve()