class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # first try
        # dict={}
        # for i in nums:
        #     dict[i]=dict.get(i,0)+1
        # return min(dict,key=dict.get)
        # optimal solution
        res = 0
        for n in nums:
            res ^= n
        return res