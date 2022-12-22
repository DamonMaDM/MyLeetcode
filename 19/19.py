
"""
删节点的时候，保持currentNode始终在被删节点的前面，注意当被删的是第一个点时
currentNode是dummyHead
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        currentNode = head
        length = 1
        while currentNode.next != None:
            currentNode = currentNode.next
            length += 1
        j = length - n
        dummyhead = ListNode(0)
        dummyhead.next = head
        currentNode = dummyhead
        while j > 0:
            currentNode = currentNode.next
            j -= 1

        currentNode.next = currentNode.next.next
        return dummyhead.next