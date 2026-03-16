class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        result = count = left = 0
        
        for right in range(len(nums)):
            if nums[right] % 2:
                k -= 1
                count = 0
            
            while not k:
                k += (nums[left] % 2)
                count += 1
                left += 1
            
            result += count
        
        return result
