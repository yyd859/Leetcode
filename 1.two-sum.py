#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #first try
        # results=[]
        # n=len(nums)
        # for i in range(0,n):
        #     remain = target - nums[i]
        #     for j in range(i+1,n):
        #         if nums[j] == remain:
        #             results=[i,j]
        #             return results
        #             break
        # OPTIMAL SOLUTION
        results=[]
        hashmap={}
        for i, value in enumerate(nums):
            remain=target - value
            if remain in hashmap:
                results=[hashmap[remain],i]
                return results
            hashmap[value] = i

        
# @lc code=end

