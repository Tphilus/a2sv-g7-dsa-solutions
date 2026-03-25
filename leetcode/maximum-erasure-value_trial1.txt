class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mx = 0
        curr_sum = 0
        left = 0
        seen = set()

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            
            curr_sum += nums[right]
            seen.add(nums[right])

            mx = max(mx, curr_sum)
        
        return mx