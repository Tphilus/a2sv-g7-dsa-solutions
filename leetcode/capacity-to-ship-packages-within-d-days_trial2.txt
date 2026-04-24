class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        res = high

        def canShip(mid):
            ships, currCap = 1, mid
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = mid
                currCap -= w
            return ships <= days


        while low <= high:
            mid = (low + high) // 2
            if canShip(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res
