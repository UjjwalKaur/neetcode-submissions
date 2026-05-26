# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        num = 1
        while curr.next:
            curr = curr.next
            num += 1

        index = num - n

        if index < 0:
            return head
        elif index == 0:
            return head.next
        else:
            curr = head
            for i in range(index):
                prev = curr
                curr = curr.next
            prev.next = curr.next
            return head


        
        