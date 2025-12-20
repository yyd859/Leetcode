# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # redo, last time not stored
        prev= None
        cur= head
        while cur:
            # 层层解，先把1和2之间解开，让1指向None 存储在一个链表里，2～5在另外一个链表里，然后长链表一个一个解开添加到reversed的链表里
            # store 2~5
            to_do = cur.next
            # unlink 1-2, cur becomes 1->None
            cur.next = prev
            # update prev
            prev=cur
            # update next cur
            cur = to_do
        return prev
