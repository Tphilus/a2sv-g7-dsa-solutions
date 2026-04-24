class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def canFinish(k):
            hours_needed = 0
            for pile in piles:
                hours_needed += (pile + k - 1) // k
            return hours_needed <= h

        while left <= right:
            mid = (left + right) // 2

            if canFinish(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left