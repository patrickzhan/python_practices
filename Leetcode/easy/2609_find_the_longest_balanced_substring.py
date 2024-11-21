class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        num_zero=0
        num_one=0
        longest=0
        length=len(s)
        for i in range(length):
            if s[i]=='0':
                num_zero+=1
                if num_one==0:
                    continue
                else:
                    if num_zero>1:
                        current_longest=2*min(num_zero-1,num_one)
                        if longest<=current_longest:
                            longest=current_longest
                        num_zero=1
                        num_one=0
                    else:
                        num_one=0
                        continue
            else:
                num_one+=1
                if i<length-1:
                    continue
                else:
                    current_longest=2*min(num_zero,num_one)
                    if longest<=current_longest:
                        longest=current_longest
        return longest
Solution1=Solution()
s="01000111"
print(Solution1.findTheLongestBalancedSubstring(s))