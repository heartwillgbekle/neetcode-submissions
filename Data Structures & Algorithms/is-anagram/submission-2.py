class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        words = defaultdict()

        for ch in s:
            words[ch] = 1 + words.get(ch, 0)

        for ch in t:
            words[ch] = words.get(ch, 0) -1
            if words[ch] < 0:
                return False
        
        return True