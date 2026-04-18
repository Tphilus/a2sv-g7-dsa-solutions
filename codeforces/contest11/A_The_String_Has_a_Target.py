t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input()
    smaller = 0
    for i in range(len(s)):
        if s[i] <= s[smaller]:
            smaller = i
    print(s[smaller] + s[:smaller] + s[smaller + 1: ])