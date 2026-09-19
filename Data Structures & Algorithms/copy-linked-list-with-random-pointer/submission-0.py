"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {None : None}
        ptr = head
        if head is None:
            return None
        while ptr:
            ptr2 = Node(ptr.val)
            mapping[ptr] = ptr2
            ptr=ptr.next
        cur=head
        while cur:
            copy = mapping[cur]
            copy.next = mapping[cur.next]
            copy.random = mapping[cur.random]
            cur=cur.next

        head2 = mapping[head]
        return head2
        



        