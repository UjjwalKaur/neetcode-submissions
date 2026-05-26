# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case: empty lists
        if not lists or len(lists) == 0:
            return None

        # use merge in merge sort technique
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # for odd number of lists, we must add this condition
                l2 = lists[i + 1] if (i + 1 < len(lists)) else None
                mergedList.append(self.mergeLists(l1, l2))
            lists = mergedList
        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = ListNode()
        pointer = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next

        pointer.next = l1 if l1 else l2

        return dummy.next


        