# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # use slow and fast pointers to find the second half
        slow = head
        fast = slow.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None

        # reverse the second half of the list
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        second = prev

        # merge the two lists
        first = head
        while second:
            # storing values in temp variables since we will be breaking the links
            temp1 = first.next
            temp2 = second.next

            # reordering based on the problem
            first.next = second
            second.next = temp1

            # shift our pointers
            first = temp1
            second = temp2




        