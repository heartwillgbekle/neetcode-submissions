class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        p = 1

        for i in range(len(nums)):
            prefix.append(p)
            p *= nums[i]
        
        output = []
        suffix = 1

        for i in range(len(nums)-1,-1,-1):
            output.append(suffix * prefix[i])
            suffix *= nums[i]

        return output[::-1]

