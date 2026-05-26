class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        counts = []

        for i, num in enumerate(accounts):
            counts.append(sum(num))
            
        return max(counts)