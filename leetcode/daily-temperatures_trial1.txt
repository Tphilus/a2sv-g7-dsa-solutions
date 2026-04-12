class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [0] * n

        for num in range(n):
            while stack and temperatures[num]> temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = num - idx

            stack.append(num)
        
        return result