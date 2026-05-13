class Solution:
    def kthCharacter(self, k: int) -> str:
        if k == 1:
            return "a"
        
        len = 1
        while len < k:
            len <<= 1
        
        return chr(ord(self.kthCharacter(k - len / 2)) + 1)