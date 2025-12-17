class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # first try, convert to number then to string
        len_input=len(digits)
        input = 0
        for key,value in enumerate(digits):
            input+=10**(len_input-key-1)*value
        plus_one=input+1
        out_put=[]
        while plus_one > 0:
            remain=plus_one-(plus_one//10)*10
            out_put.append(remain)
            plus_one=plus_one//10
        return out_put[::-1]