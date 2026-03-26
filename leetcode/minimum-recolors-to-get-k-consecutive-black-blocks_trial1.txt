class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        window = blocks[:k].count('W')
        mn = window

        for i in range(k, n):
            if blocks[i] == 'W':
                window += 1
            if blocks[i - k] == 'W':
                window -= 1
            mn = min(mn, window)
        
        return mn