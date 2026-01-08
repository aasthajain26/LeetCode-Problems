# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        a= head
        slow = a 
        if a.next is None :
            head=None
            return head
        if n==1 and a.next.next is None:
            a.next = None
            return a
        if n==2 and a.next.next is None:
            head=a.next
            return head
        while(n>0):   
            a= a.next
            n -= 1


        fast = a
        b = head
        while (fast.next is not None):
            slow= slow.next
            fast = fast.next

        new_node=slow.next.next
        slow.next =new_node
        
        return head