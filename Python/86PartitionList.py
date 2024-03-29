# LeetCode 86 Partition List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1 = h1 = ListNode(0)
        l2 = h2 = ListNode(0)
        
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head 
                l2 = l2.next 
            head = head.next
            
        l2.next = None 
        l1.next = h2.next
        
        print(h1.next.val)
        return h1.next