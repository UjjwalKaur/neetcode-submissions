# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # use a tail pointer to mark k elements
        # reverse till k
        # repeat until it iterates over k elements

        dummy = ListNode(0, head)
        groupPrev = dummy

        curr = head
        tail = head

        while True:
            kth = groupPrev
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next
            
            prev = groupNext
            curr = groupPrev.next
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # reconnecting the groups
            # most complicated part of the problem
            
            # originally the first node which becomes the last node
            tmp = groupPrev.next
            # connecting the last (originally the first) node to the first node of the next group
            groupPrev.next = kth
            # old first node now becomes the last node of the previous group
            groupPrev = tmp

        return dummy.next

        


        
        