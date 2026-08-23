class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def backtrack(index,total):
            if index==len(nums):
                return 1 if total==target else 0
            if(index,total) in memo:
                return memo[(index,total)]

            add=backtrack(index+1,total+nums[index])
            sub=backtrack(index+1,total-nums[index])

            memo[(index,total)]=add+sub
            return memo[(index,total)]

        return backtrack(0,0)

        