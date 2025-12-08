class Solution:
    #First try,success
    def isPalindrome(self, x: int) -> bool:
        # x=str(x)
        # list_f=[i for i in x]
        # list_b=[]
        # for i in list_f:
        #     list_b.insert(0,i)
        # return  True if list_f==list_b else False
    # hint: s[::-1] is the reversal of  list/string
        # x =str(x)
        # rev_x = x[::-1]
        # return  True if x==rev_x else False
    # or
        # x=str(x)
        # list_f=[i for i in x]
        # list_b=list_f.copy()
        # list_b.reverse()
        # return  True if list_f==list_b else False
    # still not the best solution but good enough, the best way with O(1) is
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10