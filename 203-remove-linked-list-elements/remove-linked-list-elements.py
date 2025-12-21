# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # first try
        # dummy=ListNode(0,head)
        # if head is None:
        #     return head
        # prev=None
        # while head:
        #     if head.val==val:
        #         if head.next is None:
        #             head.next=prev
        #         if head.next is not None:
        #             if head.next.next is None:
        #                 head.next = prev
        #             else:
        #                 head.next=head.next.next
        #     prev=head
        #     head=head.next
        # return dummy.next
        # failed
        # second try after some hint
        dummy=ListNode(0,head)
        cur=dummy
        while cur.next:
            if cur.next.val==val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return dummy.next

