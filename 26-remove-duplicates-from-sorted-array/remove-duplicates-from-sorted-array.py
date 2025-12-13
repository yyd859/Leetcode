class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # first try, dict.items() is for key and values, enumerate is for position and keys, (i in dict) is for keys only
        dict={}
        position=0
        for num in nums:
            if num not in dict:
                dict[num]=position
                position=position+1
        for key,value in dict.items():
            nums[value]=key
        return position
