from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        mx = 0
        counts = defaultdict(int)

        for right in range(len(fruits)):
            counts[fruits[right]] += 1

            while len(counts) > 2:
                counts[fruits[left]] -= 1
                if counts[fruits[left]] == 0:
                    del counts[fruits[left]]
                left += 1

            mx = max(mx, right - left + 1)

        return mx