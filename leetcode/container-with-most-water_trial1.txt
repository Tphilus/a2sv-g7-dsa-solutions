class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left

            curr_height = min(height[left], height[right])
            curr_area = width * curr_height
            mx = max(mx, curr_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return mx

