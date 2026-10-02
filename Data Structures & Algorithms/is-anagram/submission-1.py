class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        word_s = defaultdict()
        word_t = defaultdict()

        for ch in s:
            word_s[ch] = word_s.get(ch, 0) + 1
        
        for ch in t:
            word_t[ch] = word_t.get(ch, 0) + 1
        
        return word_s == word_t

        