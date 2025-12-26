class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=list(str(x))
        l=len(x)
        for i in range(0,l//2+1):
            if x[i]!=x[l-i-1]:
                return False
        return True