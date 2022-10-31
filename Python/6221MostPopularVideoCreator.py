from collections import defaultdict
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        my_dict = defaultdict()
        for i in range(len(creators)):
            if creators[i] not in my_dict:
                my_dict[creators[i]] = [views[i], ids[i], views[i]]
            else:
                my_dict[creators[i]][0] += views[i]
                if my_dict[creators[i]][2] < views[i]:
                    my_dict[creators[i]][2] = views[i]
                    my_dict[creators[i]][1] = ids[i]
                elif my_dict[creators[i]][2] == views[i]:
                    if my_dict[creators[i]][1] > ids[i]:
                        my_dict[creators[i]][1] = ids[i]
        mx = 0
        for i in my_dict:
            mx = max(mx, my_dict[i][0])
        res = []
        for i in my_dict:
            if my_dict[i][0] == mx:
                res.append([i, my_dict[i][1]])
        return res
        # max_key = max(sorted_dict, key=sorted_dict.get)
        # print(max_key)