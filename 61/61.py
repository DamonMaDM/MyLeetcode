
"""
第一种把list变成一个ring
第二种用dummyHead
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        l = 1
        tail = head
        while tail.next != None:
            l += 1
            tail = tail.next
        tail.next = head

        newTail = l-k%l
        new = head
        for i in range(newTail-1):
            new = new.next
        newHead = new.next
        new.next = None

        return newHead



# class Solution:
#     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if head == None or head.next == None:
#             return head
#         l = 1
#         tail = head
#         while tail.next != None:
#             l += 1
#             tail = tail.next
#         tail.next = head
#         k = k % l
#         if k==0:
#             return head
#         dummyhead = ListNode(0)
#         dummyhead.next = head
#         aheadNode = dummyhead

#         for i in range(l-k):
#             aheadNode = aheadNode.next
#         ans = aheadNode.next
#         aheadNode.next = None
#         tail.next = head
#         return ans