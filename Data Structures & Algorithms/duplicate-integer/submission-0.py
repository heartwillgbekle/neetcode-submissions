class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = set()
        count = 0
        for num in nums:
            if num not in values:
                values.add(num)
            else:
                count += 1

        return False if count == 0 else True
        