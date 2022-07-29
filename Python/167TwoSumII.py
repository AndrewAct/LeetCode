class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow = 0 
        n = len(numbers)
        fast = n-1
        # res = [0,0]
        while (slow<fast):
            if (numbers[slow]+numbers[fast])==target:
                return [slow+1, fast+1]
            elif (numbers[slow]+numbers[fast])<target:
                slow += 1
            else:
                fast -= 1