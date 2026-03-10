class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
        mx = float("-inf")

        for i in range(k):
            window_sum += nums[i]
        
        mx = window_sum
        left = 0
        
        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[left]

            mx = max(mx, window_sum)
            left += 1
        
        return mx / k