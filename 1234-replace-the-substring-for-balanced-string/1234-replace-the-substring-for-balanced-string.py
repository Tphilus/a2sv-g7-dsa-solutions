class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n / 4

        freq = Counter(s)
        if all(freq[count] == target for count in 'QWER'):
            return 0
            
        left = 0
        mn = n

        for right in range(n):
            freq[s[right]] -= 1

            while left <= right and all(freq[count] <= target for count in 'QWER'):
                mn = min(mn, right - left + 1)
                freq[s[left]] += 1
                left += 1
        
        return mn