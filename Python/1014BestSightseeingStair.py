class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxSoFar, res = values[0], 0 
        n = len(values)
        for i in range(1, n):
            res = max(res, maxSoFar + values[i] - i)
            maxSoFar = max(maxSoFar, values[i] + i)
        return res 