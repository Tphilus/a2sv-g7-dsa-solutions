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
    

# Code 2
    
# Step 1: Read number of test cases
t = int(input())

# Step 2: Loop through each test case
for _ in range(t):
    s = input().strip()
    
    # Step 3.1: Build Frequency Map
    # We use an array of size 26 because there are 26 lowercase letters.
    # ord('a') is 97. Subtract 97 to map 'a' to 0, 'b' to 1, etc.
    freq = [0] * 26
    for char in s:
        freq[ord(char) - ord('a')] += 1
        
    # Example for "abcabdc":
    # freq['a'] = 2, freq['b'] = 2, freq['c'] = 2, freq['d'] = 1

    # Step 3.2: Scan from left to right to find the stopping point
    stop_index = 0
    
    for i in range(len(s)):
        char_code = ord(s[i]) - ord('a')
        
        # Check if this is the LAST occurrence of this character
        if freq[char_code] == 1:
            stop_index = i
            break # We found our stopping point! Exit the loop.
        else:
            # If it's not the last occurrence, the algorithm would remove it.
            # We simulate the removal by decrementing the count.
            freq[char_code] -= 1

    # Step 3.3: Output the substring
    # The answer is everything from the stop_index to the end.
    print(s[stop_index:])