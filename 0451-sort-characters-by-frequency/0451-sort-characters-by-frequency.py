class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        res = ""

        for char, freq in counts.most_common():
            res += char * freq
        
        return res