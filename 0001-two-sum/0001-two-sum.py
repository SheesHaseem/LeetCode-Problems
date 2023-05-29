class Solution:
    def twoSum(self, nums, target):
        numset = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in numset:
                return [numset[target - nums[i]], i]
            else:
                numset[nums[i]] = i
        return []