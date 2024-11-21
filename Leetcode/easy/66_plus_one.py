class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits_size=len(digits)
        for i in range(digits_size):
                location=-1-i
                print(f"current location is {location},current value is {digits[location]}")
                if location==-1:
                    if digits[-1]==9:
                        digits[-1]=0
                        if digits_size==1:
                            return [1,0]
                        else:
                            continue
                    else:
                        digits[-1]=digits[-1]+1
                        return digits
                if digits[location]!=9:
                     digits[location]=digits[location]+1
                     return digits
                elif location!=-digits_size:
                     digits[location]=0
                     continue
                else:
                     return [1 if k == 0 else 0 for k in range(digits_size+1)]


                    
Solution1=Solution()
digits_exam=[9]
result=Solution1.plusOne(digits_exam)
print(result)