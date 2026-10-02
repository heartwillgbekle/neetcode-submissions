class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     mid = (l + r) // 2 
        #     if nums[mid] > target:
        #         r = mid - 1

        #     elif nums[mid] < target:
        #         l = mid + 1

        #     else:
        #         return mid
        # return -1

        if not nums:
            return -1

        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.search(nums[:mid], target)
        else:
            res = self.search(nums[mid+1:], target)
            return -1 if res == -1 else (mid + 1 + res)

    

        

        