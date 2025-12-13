class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dict={}
        position=0
        for num in nums:
            if num not in dict:
                dict[num]=position
                position=position+1
        nums[:]=[0]*len(nums)
        for key,value in dict.items():
            nums[value]=key
        return position
