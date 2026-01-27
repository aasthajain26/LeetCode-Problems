# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummynode = ListNode()
        head3=dummynode
        
        
        while(list1 and list2):
            if list1.val<list2.val:
                dummynode.next = list1
                list1=list1.next
            else:
                dummynode.next=list2
                list2=list2.next

            dummynode=dummynode.next

        if list1:
            dummynode.next=list1
        elif list2:
            dummynode.next=list2
            
        return head3.next