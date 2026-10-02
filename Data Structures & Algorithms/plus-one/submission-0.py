class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""

        for x in digits:
            num += str(x)

        new = int(num) + 1
        res = []

        for x in str(new):
            res.append(int(x))

        return res
        