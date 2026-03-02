class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        diff = []
        output = []

        for num in arr1:
            if num not in arr2:
                diff.append(num)
        
        diff.sort()
        counts = Counter(arr1)
        
        for num in arr2:
            for i in range(counts[num]):
                output.append(num)
        
        return output + diff