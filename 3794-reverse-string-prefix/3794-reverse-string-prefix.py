class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        # print(s[:k])
        # print(s[k:])
        return s[:k][::-1] + s[k:]
            