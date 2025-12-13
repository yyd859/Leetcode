class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # first try, know it's not the best way, time complexity N+NlogN
        # for i in range(0,n):
        #     nums1[m+i]=nums2[i]
        # nums1.sort()
        #second try, after some hints from gpt to use multiple pointers
        i = m-1 # last of nums1 (un-merged)
        j = n-1 # last of nums2
        k = m+n-1 # last of final nums1
        if m==0:
            nums1[:]=nums2
            return
        while i>=0 and j>=0:
            if nums1[i]<nums2[j]:
                nums1[k]=nums2[j]
                j-=1
            else:
                nums1[k]=nums1[i]
                i-=1
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1
        return
