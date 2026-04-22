class Solution:
    def rob(self, nums: List[int]) -> int:
        # if the length of nums is 1, just return that value
        if len(nums) == 1:
            return nums[0]
        
        # we need to memoize for two different runs, one including the first value and one excluding
        memo = [[-1] * 2 for _ in range(len(nums))]

        def dp(i, flag):
            # if i is greater than nums or if the flag is on and we can't get the last one, we return 0
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            
            # memoize that specific case with the flag
            if memo[i][flag] != -1:
                return memo[i][flag]
            
            # skip and rob logic is the exact same
            skip = dp(i + 1, flag)
            rob = dp(i + 2, flag) + nums[i]

            # set and return the max option
            memo[i][flag] = max(skip, rob)

            return memo[i][flag]

        # we do two runs, one where we include 0th index and set flag is True and one which we don't
        return max(dp(0, True), dp(1, False))