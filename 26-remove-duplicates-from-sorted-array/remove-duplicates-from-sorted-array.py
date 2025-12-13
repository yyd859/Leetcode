class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # first try, dict.items() is for key and values, enumerate is for position and keys, (i in dict) is for keys only
        # dict={}
        # position=0
        # for num in nums:
        #     if num not in dict:
        #         dict[num]=position
        #         position=position+1
        # for key,value in dict.items():
        #     nums[value]=key
        # return position
        # second try: two pointers after hint from gpt
        if not nums:
            return 0
        slow = 1  # 下一个写入位置
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow - 1]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
