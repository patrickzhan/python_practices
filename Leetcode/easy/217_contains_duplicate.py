class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n=len(nums)
        nums_dict={}
        for num in nums:
            if num in nums_dict:
                nums_dict[num]+=1
            else:
                nums_dict[num]=1
            if nums_dict[num]==2:
                return True
        return False


sol1=Solution()
nums=[1,2,3,1]
result=sol1.containsDuplicate(nums)
print(result)