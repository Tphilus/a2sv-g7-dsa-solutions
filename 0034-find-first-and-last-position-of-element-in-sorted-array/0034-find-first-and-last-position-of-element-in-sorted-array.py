class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(target):
            low, high = 0, len(nums) - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return low
        
        first = search(target)
        last = search(target + 1) - 1

        if first <= last:
            return [first, last]
        
        return [-1, -1]
