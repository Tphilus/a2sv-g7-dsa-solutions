class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sett = set(nums)
        mx = 0

        if len(sett) < 3:
            return max(sett)
        
        arr = sorted(sett)
        return arr[-3]
