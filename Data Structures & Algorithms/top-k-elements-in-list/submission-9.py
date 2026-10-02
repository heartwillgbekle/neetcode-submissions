class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mynums = defaultdict()
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            mynums[num] = mynums.get(num, 0) + 1

        for key, val in mynums.items():
            freq[val] += [key]

        for i in range(len(freq)-1, -1,-1):
            for x in freq[i]:
                res.append(x)
            if len(res) == k:
                return res
            
                


        