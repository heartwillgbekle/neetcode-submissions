class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mystrs = defaultdict()
        

        for word in strs:
            cha = [0]*26
            for x in word:
                cha[ord(x) - ord("a")] += 1

            key = tuple(cha)

            if key in mystrs:
                mystrs[key].append(word)
            else:
                mystrs[key] = [word]

        return list(mystrs.values())
            
        