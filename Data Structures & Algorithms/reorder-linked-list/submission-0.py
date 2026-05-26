# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        length = 0
        prev = {}
        while curr.next:
            prev[curr.next] = curr
            curr = curr.next
            length += 1
        tail = curr

        curr = head
        start = head.next
        end = tail
        i = 1
        while i <= length:
            curr.next = tail
            tail = prev[tail]
            curr = curr.next

            curr.next = start
            start = start.next
            curr = curr.next
            
            i = i + 2
        curr.next = None

        