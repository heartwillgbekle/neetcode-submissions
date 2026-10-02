class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mynums = defaultdict()

        for i, num in enumerate(nums):
            complement = target - num
            if complement in mynums:
                return [mynums[complement], i]
            else:
                mynums[num] = i
        