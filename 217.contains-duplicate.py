#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    #First Try，O(N)
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for _,value in enumerate(nums):
            if value in dict:
                return True
            else: dict[value] = True
        return False
        
# @lc code=end

