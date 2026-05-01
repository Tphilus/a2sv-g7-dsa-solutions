class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hourWeNeed(k):
            hour = 0
            for pile in piles:
                hour += pile // k
                if pile % k:
                    hour += 1
            return hour
    
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            
            if hourWeNeed(mid) <= h:
                high = mid
            else:
                low = mid + 1

        return low