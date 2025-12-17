class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # first try
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i]=1
            dict[i]+=1
        max_vote=0
        major=0
        for key,value in dict.items():
            if value > max_vote:
                max_vote=value
                major=key
        return major

        