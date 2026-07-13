class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pro=nums[0]
        prmaxsub=nums[0]
        prminsub=nums[0]
        for i in range(1,len(nums)):
            maxsub=prmaxsub
            minsub=prminsub
            prmaxsub=max(maxsub*nums[i],nums[i],minsub*nums[i])
            prminsub=min(maxsub*nums[i],nums[i],minsub*nums[i])
            pro=max(pro,prmaxsub)
        return pro