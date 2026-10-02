class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}

        for x in nums:
            dict1[x] = dict1.get(x, 0) + 1

        for i, x in dict1.items():
            if x > 1:
                return True

        return False
        