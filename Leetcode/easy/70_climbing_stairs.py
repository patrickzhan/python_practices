from math import factorial as fac
class Solution:
    def climbStairs(self, n: int) -> int:
        ways=0
        num_two=n//2
        num_one=n%2
        current=int(fac(num_two+num_one)/(fac(num_two)*fac(num_one)))
        ways+=current
        while num_two>0:
            num_two-=1
            num_one+=2
            current=int(fac(num_two+num_one)/(fac(num_two)*fac(num_one)))
            ways+=current
        return ways
Solution1=Solution()
n=3
print(Solution1.climbStairs(n))
