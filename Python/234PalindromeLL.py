# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        left, right = head, head 
        while left:
            stack.append(left.val)
            left = left.next 
            
        while right:
            if right.val == stack.pop():
                right = right.next 
            else:
                return False 
        
        return True
        