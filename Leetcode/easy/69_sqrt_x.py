
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=2**31-1
        
        while True:
            ans=math.floor((low+high)/2)
            if ans**2<=x and (ans+1)**2>x:
                return ans
            else:
                if ans**2<x:
                    low=ans
                else:
                    high=ans


Solution1=Solution()
x=2**16+2**9
print(Solution1.mySqrt(x))