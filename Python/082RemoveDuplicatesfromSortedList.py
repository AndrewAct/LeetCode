# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        # print(head)
        while cur:
            if cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next 
                # print(cur)
            cur = cur.next
            # print(head)
        return head 