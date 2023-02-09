class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 
        right = len(height)- 1 
        leftMax = height[left]
        rightMax = height[right]
        vol = 0
        while left < right:
            if (leftMax < rightMax):
                vol += leftMax - height[left]
                left += 1
                leftMax = max(leftMax, height[left])
            else:
                vol += rightMax - height[right]
                right -= 1 
                rightMax = max(rightMax, height[right])
        return vol
        