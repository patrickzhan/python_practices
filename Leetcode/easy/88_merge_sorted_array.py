class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return
        if m==0:
            for k in range(n):
                nums1[k]=nums2[k]
            return
        j=0
        for i in range(n):
            if nums2[i]<=nums1[0]:
                nums1.insert(0,nums2[i])
                m+=1
                continue
            if nums2[i]>=nums1[m-1]:
                nums1[m:m]=nums2[i:n]
                m+=(n-i)
                break

            while j<m:
                if nums1[j]<=nums2[i] and nums2[i]<=nums1[j+1]:
                    nums1.insert(j+1,nums2[i])
                    m+=1
                    break
                j+=1
        del nums1[-n:]
        return
Solution1=Solution()
nums1=[4,5,6,0,0,0]
nums2=[1,2,3]
m=3
n=3
Solution1.merge(nums1,m,nums2,n)
print(nums1)
