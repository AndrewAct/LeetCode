import heapq
import math 

class Solution:
    def pickGifts(self, gifts, k):
        # Negatizing all values in gifts since heappop will pop the smallest value
        res = [-i for i in gifts]
        heapq.heapify(res)
        for i in range(k):
            tmp = -heapq.heappop(res)
            tmp = int(math.sqrt(tmp))
            heapq.heappush(res, -tmp)
        ans = [-i for i in res]
        return int(sum(ans))       