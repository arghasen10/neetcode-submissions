# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        # if head.next.next is None:
        #     return False
        head1 = head
        head2 = head
        while head1 and head2:
            head1 = head1.next
            try:
                head2 = head2.next.next
            except AttributeError as e:
                return False
            if head1 == head2:
                return True
        return False