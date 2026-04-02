class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 0

        for num in arr:
            if num > prev:
                prev += 1
        
        return prev