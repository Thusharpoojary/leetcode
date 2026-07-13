class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        maxSub=nums[0]
        for i in range(1,len(nums)):
            maxSub=max(maxSub+nums[i],nums[i])

            res=max(res,maxSub)
        return res
        