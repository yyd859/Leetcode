#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #first try, failed with a small typo
        dict_s={}
        dict_t={}
        for i in list(s):
            if i not in dict_s:
                dict_s[i] = 0
            dict_s[i]+=1
        for i in list(t):
            if i not in dict_t:
                dict_t[i] = 0
            dict_t[i]+=1
        result= False
        if len(s)==len(t) and dict_s==dict_t:
            result = True
        return result
# @lc code=end

