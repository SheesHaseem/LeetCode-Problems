class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1]*n
        x = 1
        y = 1
        z = 1
        for i in range(n):
            answer[i] *= x
            x = x*nums[i]
            answer[n-i-1] *= y
            y = y*nums[n-i-1]
        return answer