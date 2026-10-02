class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dicts = {}
        dictt = {}

        for x in s:
            dicts[x] = dicts.get(x, 0) + 1

        
        for x in t:
            dictt[x] = dictt.get(x, 0) + 1

        return dicts == dictt
