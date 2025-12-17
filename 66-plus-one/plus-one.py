class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # first try, convert to number then to string, out of memory 
        # len_input=len(digits)
        # input = 0
        # for key,value in enumerate(digits):
        #     input+=10**(len_input-key-1)*value
        # plus_one=input+1
        # out_put=[]
        # while plus_one > 0:
        #     remain=plus_one-(plus_one//10)*10
        #     out_put.append(remain)
        #     plus_one=plus_one//10
        # return out_put[::-1]
        # second try, after glancing at the best solution
        n=len(digits)
        for i in range(n-1,-1,-1):
            # if not 9, plus one
            if digits[i]!=9:
                digits[i] += 1
                return digits
            else:
                # if 9, make the position 0 and leave it to the next position go into the loop
                digits[i]=0
                # if all 9s. just add 1 at the very front
        return [1]+digits
            