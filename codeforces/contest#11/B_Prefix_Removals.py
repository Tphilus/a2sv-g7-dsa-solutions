t = int(input())
for _ in range(t):
    s = input()
    
    # Count Frequences 
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Find where to stop 
    stop_idx = 0
    for num in range(len(s)):
        if freq[s[num]] == 1:
            stop_idx = num
            break
        
        freq[s[num]] -= 1
    
    print(s[stop_idx:])