class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1 or len(nums) == 1:
            return nums 
        res = [-10000] * (len(nums) - k + 1)
        dq = deque([0])

        for i in range(1, len(nums)):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i - dq[0] >= k:
                dq.popleft()
            if i >= k-1:
                res[i-k+1] = nums[dq[0]]
        return res 