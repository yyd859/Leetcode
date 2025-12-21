class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs)
        l=len(strs[0])
        delete=0
        fixed=[False]*(n-1)
        for j in range(0,l):
            need_delete=False
            for i in range(0,n-1):
                if not fixed[i] and strs[i][j]>strs[i+1][j]:
                    need_delete=True
                    break
            if need_delete:
                delete+=1
                continue
            for i in range(0,n-1):
                if not fixed[i] and strs[i][j]<strs[i+1][j]:
                    fixed[i]=True
        return delete
                