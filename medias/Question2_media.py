class Solution:
    def rob(self, nums):
        memo = {}

        def recursiveRob(i):
            if i >= len(nums):
                return 0 
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + recursiveRob(i + 2), recursiveRob(i + 1))
            return memo[i]

        return recursiveRob(0)
