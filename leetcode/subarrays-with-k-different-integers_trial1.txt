class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cnt, result, left, mx = [0] * (len(nums) + 1), 0, 0, 0
        for n in nums:
            cnt[n] += 1
            if cnt[n] == 1:
                k -= 1
                if (k < 0):
                    cnt[nums[mx]] = 0
                    mx += 1
                    left = mx
            if k <= 0:
                while(cnt[nums[mx]] > 1):
                    cnt[nums[mx]] -= 1
                    mx += 1
                result += mx - left + 1
        return result