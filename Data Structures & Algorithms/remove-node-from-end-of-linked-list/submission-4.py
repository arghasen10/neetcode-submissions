# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        list_n=1
        while ptr.next:
            ptr=ptr.next
            list_n+=1
        to_remove=list_n-n+1
        i=1
        ptr=head
        while i < to_remove-1:
            ptr=ptr.next
            i+=1
        if list_n == 1:
            return None
        if to_remove == 1:
            head = head.next
            return head
        ptr.next = ptr.next.next
        return head

        
        