
"""
类似第九题，注意重新定义连接时，node和node不要连错

 o     o     o    o 有三条新的连接
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        dummyHead.next = head
        current = dummyHead
        while current != None:
            if current.next == None or current.next.next == None:
                break
            else:
                temprory = current.next
                current.next = current.next.next
                temprory.next = current.next.next
                current.next.next = temprory
            current = current.next.next
        return dummyHead.next