class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        position = 0

        for i in range(2, n + 1):
            position = (position + k) % i
        
        return position + 1