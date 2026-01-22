# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head and head.val == val:
            head = head.next
        a=head
        prev=None
        
        while(a):
            curr=a
            if a.val==val:
                nxt= a.next
                prev.next = nxt
            else:

                prev=curr
        
            a=a.next

        return head
