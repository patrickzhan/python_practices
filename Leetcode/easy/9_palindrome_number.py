class Solution:
    def isPalindrome(self, x:int) -> bool:
        if x<0:
            return False
        else:
            string_x=list(str(x))
            print(string_x)
            if x<10:
                return True
            elif x<1000:
                if string_x[0]!=string_x[-1]:
                    return False
            for i in range(len(string_x)//2):
                print(string_x[i],string_x[len(string_x)-1-i])
                if string_x[i]!=string_x[len(string_x)-1-i]:
                    return False
            return True
sol1=Solution()
x=1000000001
print(sol1.isPalindrome(x))