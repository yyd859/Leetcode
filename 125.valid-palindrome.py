#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first try,success
        s = "".join(filter(str.isalnum, s)).lower()
        result=True
        for i in range(0,len(s)//2):
            if s[i]!=s[len(s)-1-i]:
                result = False
                break
        return result
        # optimal solution in space complexity
        # left, right = 0, len(s) - 1

        # while left < right:
        #     # 跳过非字母数字
        #     while left < right and not s[left].isalnum():
        #         left += 1
        #     while left < right and not s[right].isalnum():
        #         right -= 1

        #     # 比较（忽略大小写）
        #     if s[left].lower() != s[right].lower():
        #         return False

        #     left += 1
        #     right -= 1

        return True

# @lc code=end

