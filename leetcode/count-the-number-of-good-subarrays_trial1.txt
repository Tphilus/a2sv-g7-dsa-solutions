class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        same, right = 0, -1
        count = Counter()
        result = 0

        for left in range(n):
            while same < k and right + 1 < n:
                right += 1
                same += count[nums[right]]
                count[nums[right]] += 1
            
            if same >= k:
                result += n - right
            count[nums[left]] -= 1
            same -= count[nums[left]]
        
        return result
