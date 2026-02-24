class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [""] * len(s)

        for idx, char in enumerate(s):
            res[indices[idx]] = char
        
        return "".join(res)
