class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 * n):
            idx = i % n

            while stack and nums[idx] > nums[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = nums[idx]

            if i < n:
                stack.append(idx)

        return result