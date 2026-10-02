class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word

        return res

    def decode(self, s: str) -> List[str]:
        l = r = 0
        res = []

        while r < (len(s)):

            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            start = r + 1
            end = length + start

            res.append(s[start:end])
            l = r = end

        return res

