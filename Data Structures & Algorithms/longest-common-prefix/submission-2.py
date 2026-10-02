class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs[0]:
            return ""
        res = ""

        cur = strs[0][0]
        for i in range(len(strs[0])):
            for word in strs:
                if cur == word[:i+1]:
                    continue
                else:
                    return res

            res = cur
            cur = word[:i+2]

        return res


        