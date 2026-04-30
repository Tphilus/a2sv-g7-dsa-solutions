class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        
        starts = [(intervals[i][0], i) for i in range(n)]
        starts.sort() 
        
        result = [-1] * n
        
        for i in range(n):
            end_i = intervals[i][1]
            
            left, right = 0, n - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if starts[mid][0] >= end_i:
                    idx = starts[mid][1]   
                    right = mid - 1 
                else:
                    left = mid + 1  
            
            result[i] = idx
        
        return result