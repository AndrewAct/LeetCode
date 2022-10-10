class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_part = nums[:n]
        second_part = nums[n:]
        # assert len(nums) == n*2
        res = []
        for i in range(n):
            res.append(first_part[i])
            res.append(second_part[i])
        return res 