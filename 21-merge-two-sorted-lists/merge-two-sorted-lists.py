# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # first try
        # 初步思路类似双指针，开一个全新的链表，上下链表的val对比，哪个小就把当前值放进新建的链表（一样的话无所谓），然后指针向右移动，直到其中任意一个链表next是空了
        # dummy=ListNode(0)
        # result = dummy
        # while list1 or list2:
        #     if list1 and list1.val<=list2.val:
        #         nxt=list1.next
        #         element = list1
        #         element.next= None
        #         result.next = element
        #         list1=nxt
        #     else: 
        #         nxt=list2.next
        #         element = list2
        #         element.next= None
        #         result.next = element
        #         list2=nxt
        # return result.next
        #failed, 这种写法没法快速定位到result的最后一位
        # result=result.next可以挪一位指针从而保留前面的节点
        dummy = ListNode(0)
        result = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next  # ✅ 尾指针往后走

        # ✅ 把剩下的直接接上（其中一个必然非空或都空）
        result.next = list1 if list1 else list2

        return dummy.next
        #链表里，a=b.next,如果.next在等号右边那就是移动指针，你赋值的还是整个链；如果是a.next=b，才是拼接链条