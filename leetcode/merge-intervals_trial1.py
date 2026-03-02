class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        marged = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                marged.append(prev)
                prev = interval

        marged.append(prev)

        return marged
        
