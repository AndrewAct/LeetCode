class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {'2':'abc',
              '3':'def',
              '4':'ghi',
              '5':'jkl',
              '6':'mno',
              '7':'pqrs',
              '8':'tuv',
              '9':'wxyz'}
        def dfs(i = 0, combo = "", res = []):
            if i == len(digits):
                res.append(combo)
            else:
                nextDigit = digits[i]
                children = dic[nextDigit]
                for child in children:
                    dfs(i+1, combo + child, res)
            return res 
        return dfs(0, "", [])