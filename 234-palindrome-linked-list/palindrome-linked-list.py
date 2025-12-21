# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #first try
        # slow=head
        # fast=head
        # while fast.next is not None:
        #     fast=fast.next
        # while slow.next !=fast.previous:
        #     if slow.val!=fast.val:
        #         return false
        #     else:
        #         slow=slow.next
        #         fast=fast.previous
        # return true
        # 可以直接反转链表做吗？
        # second try
        # prev = None
        # cur = head
        # while cur:
        #     nxt=cur.next
        #     cur.next=prev
        #     prev=cur
        #     cur=nxt
        # forward=head
        # reverse=prev
        # while forward:
        #     if forward.val !=reverse.val:
        #         return False
        #     else:
        #         forward=forward.next
        #         reverse=reverse.next
        # return True
        # failed because as cur is being updated, head is also changed, forward= head is not copying the original linked list
        # 这题需要3步，1.找中点 2. 反转后半段 3. 比较前半段和后半段
        #1. 找中点
        slow = fast =head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #2.reverse right half
        prev=None
        cur=slow
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        # 3. compare left and right
        left = head
        right = prev
        while left and right:
            if left.val != right.val:
                return False
            else:
                left=left.next
                right=right.next
        return True
