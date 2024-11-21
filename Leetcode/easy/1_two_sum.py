class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
sol1 = Solution()
nums1 =[2,7,11,15]
target1=9
sol11 = sol1.twoSum(nums1, target1)
print(sol11)