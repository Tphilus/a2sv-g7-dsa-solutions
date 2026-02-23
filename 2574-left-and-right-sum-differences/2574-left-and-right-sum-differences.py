class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        res = [0] * len(nums)
        sum_ = sum(nums)

        for i in range(len(nums)):
            sum_ -= nums[i]
            res[i] = abs(left - sum_)
            left += nums[i]

        return res
