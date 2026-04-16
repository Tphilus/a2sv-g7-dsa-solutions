class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        stack.append(0)
        heights.append(0)

        for i, currHeight in enumerate(heights):
            while stack and heights[stack[-1]] > currHeight:
                localMaxHeight = heights[stack.pop()]
                width = 0

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                maxArea = max(maxArea, localMaxHeight * width)
            stack.append(i)
        
        return maxArea