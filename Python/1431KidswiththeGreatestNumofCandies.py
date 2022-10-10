class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        res = []
        max_candy = max(candies)
        for num in candies:
            res.append(num == max_candy or (extraCandies + num) >= max_candy)
        return res 