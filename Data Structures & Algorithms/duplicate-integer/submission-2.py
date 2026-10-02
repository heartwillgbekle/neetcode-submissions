class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mynums = defaultdict()

        for num in nums:
            mynums[num] = 1 + mynums.get(num, 0)

        for key, val in mynums.items():
            if val >= 2:
                return True

        return False