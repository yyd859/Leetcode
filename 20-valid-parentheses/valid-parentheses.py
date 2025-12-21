class Solution:
    def isValid(self, s: str) -> bool:
        # first try
        # b1=0
        # b2=0
        # b3=0
        # result=True
        # for i in s:
        #     if i == '(':
        #         b1+=1
        #     if i == ')':
        #         b1-=1
        #     if i == '{':
        #         b2+=1
        #     if i == '}':
        #         b2-=1
        #     if i == '[':
        #         b3+=1
        #     if i == ']':
        #         b3-=1
        #     if b1<0 or b2<0 or b3<0:
        #         result=False
        #         break
        # if b1!=0 or b2!=0 or b3!=0:
        #     result=False
        # return result
        # 要用mapping和stack做
        stack=[]
        mapping={')':'(','}':'{',']':'['}
        for i in s:
            if i in mapping.values():
                stack.append(i)
            if i in mapping:
                #这里stack.pop会改变stack，实际就是把最上面（最后添加的）拿走了
                if not stack or stack.pop()!=mapping[i]:
                    return False
        return not stack
