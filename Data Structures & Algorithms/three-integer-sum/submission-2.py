from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # If the current number is > 0, no three numbers can sum to 0
            if nums[i] > 0:
                break

            # Skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicates for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return res

        