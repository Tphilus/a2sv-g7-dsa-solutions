class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        first  = 0
        lng_prefix = 0

        while first < len(s) and lng_prefix < len(t):
            if s[first] == t[lng_prefix]:
                lng_prefix += 1
            first += 1
        
        return len(t) - lng_prefix