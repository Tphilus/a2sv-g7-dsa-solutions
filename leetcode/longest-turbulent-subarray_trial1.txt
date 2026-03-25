class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        result = 1
        n = len(arr)
        for right in range(1, n):
            if arr[right-1] == arr[right]:
                result = max(result, 1)
                left = right
            elif right+1 < n and not (arr[right-1] < arr[right] > arr[right+1]) and not (arr[right-1] > arr[right] < arr[right+1]):
                result = max(right - left + 1, result)
                left = right
            else:
                result = max(right-left+1, result)
        return result