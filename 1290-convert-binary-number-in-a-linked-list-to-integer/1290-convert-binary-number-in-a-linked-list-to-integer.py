# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr = head
        count = 0
        while curr:
            count = (count * 2) + curr.val
            curr = curr.next
        
        return count
            