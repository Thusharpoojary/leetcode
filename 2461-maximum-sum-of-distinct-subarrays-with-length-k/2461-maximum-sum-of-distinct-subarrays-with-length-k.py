class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        winsum = 0
        ans = 0

        for i in range(len(nums)):
            winsum += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            if i >= k:
                winsum -= nums[i - k]
                freq[nums[i - k]] -= 1
                if freq[nums[i - k]] == 0:
                    del freq[nums[i - k]]

            if i >= k - 1 and len(freq) == k:
                ans = max(ans, winsum)

        return ans