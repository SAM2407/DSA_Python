# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        flag = False
        if head is None:
            return None
        slow,fast = head,head
        while fast and fast.next:
            slow  = slow.next
            fast= fast.next.next
            if slow == fast:
                flag = True
                break
        if  not flag:
            return None

        pos = head
        while pos is not slow:
            pos=pos.next
            slow=slow.next

        return pos
        
