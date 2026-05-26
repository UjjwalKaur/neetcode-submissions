# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # keep a dict for visited nodes 
        # like checking for duplicates in an integer list
        curr = head
        visited = {}
        while (curr):
            if (curr.next in visited):
                return True
            else:
                visited[curr.next] = curr
            curr = curr.next

        return False

        
        