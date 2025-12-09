#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # first try, success
        # dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # s=list(s)
        # result_list=[dict[i] for i in s][::-1]
        # for i in range(1,len(result_list)):
        #     if result_list[i-1]>result_list[i]:
        #         result_list[i]=result_list[i]*(-1)
        # return sum(result_list)
        #best solution
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for i in range(len(s)):
            # 如果当前值 < 下一个值，就减，否则加
            if i < len(s) - 1 and d[s[i]] < d[s[i + 1]]:
                result -= d[s[i]]
            else:
                result += d[s[i]]
        
        return result
# @lc code=end

