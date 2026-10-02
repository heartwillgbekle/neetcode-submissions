class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        i = j = 0

        while j < len(nums):
            if nums[i] not in seen:
                seen.add(nums[i])

            while j < len(nums) and nums[j] in seen:
                j += 1

            if j < len(nums) and nums[j] not in seen:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return i + 1

            

            

            


        