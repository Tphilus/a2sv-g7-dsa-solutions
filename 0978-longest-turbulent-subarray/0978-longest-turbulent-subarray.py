class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        result = 1

        for right in range(1, n):
            curr = arr[right] - arr[right - 1]
            prev = arr[right-1] - arr[right-2] if right > 1 else None

            if curr == 0:
                left = right         
            elif prev is not None and (prev > 0) == (curr > 0):
                left = right - 1      
            result = max(result, right - left + 1)

        return result