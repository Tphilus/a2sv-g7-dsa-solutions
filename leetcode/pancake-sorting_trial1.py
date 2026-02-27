class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        output = []

        for target in range(n, 0, -1):
            i = arr.index(target)

            if i == target - 1:
                continue
            
            if i != 0:
                arr[:i+1] = arr[:i+1][::-1]
                output.append(i+1)
            
            arr[:target] = arr[:target][::-1]
            output.append(target)
        
        return output