class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        freq = [0]*(max(nums)+1)
        for n in nums:
            freq[n] += n
        dp = [0]*len(freq)
        dp[1] = freq[1]
        for i in range(2,len(dp)):
            dp[i] = max(dp[i-2]+freq[i],dp[i-1])
        return dp[-1]