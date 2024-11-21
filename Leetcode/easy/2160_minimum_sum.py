class Solution:
    def minimumSum(self, num: int) -> int:
        num_list=list(str(num))
        a=min(num_list)
        num_list.remove(a)
        b=min(num_list)
        num_list.remove(b)
        sum=(int(a)+int(b))*10+int(num_list[0])+int(num_list[1])
        return sum
Solution1=Solution()
num=1234
print(Solution1.minimumSum(num))