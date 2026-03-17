class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        current_vowels = 0
        
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        
        mx = current_vowels
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels += 1
            
            if s[i - k] in vowels:
                current_vowels -= 1
            
            mx = max(mx, current_vowels)
                
            if mx == k:
                return k
                
        return mx