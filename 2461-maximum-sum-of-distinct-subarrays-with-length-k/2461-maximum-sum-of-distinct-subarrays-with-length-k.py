class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        results = 0
        current_sum = 0
        left = 0
        right = 0
        seen = {}

        while right < len(nums):
            curr_num = nums[right]
            last_occurrence = seen.get(curr_num, -1)
            while left <= last_occurrence or right - left + 1 > k:
                current_sum -= nums[left]
                left += 1
            seen[curr_num] = right
            current_sum += nums[right]
            if right - left + 1 == k:
                results = max(results, current_sum)
            right += 1
        return results