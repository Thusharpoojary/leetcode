class Solution:
    def maxProduct(self, nums: List[int]):
        pro = nums[0]
        maxsub = nums[0]
        minsub = nums[0]

        for i in range(1, len(nums)):
            prevMax = maxsub
            prevMin = minsub

            maxsub = max(prevMax * nums[i], nums[i], prevMin * nums[i])
            minsub = min(prevMax * nums[i], nums[i], prevMin * nums[i])

            pro = max(pro, maxsub)

        return pro