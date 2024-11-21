# class Solution:
#     def romanToInt(self, s:str) -> int:
#         tag=list(reversed(s))
#         n=len(tag)
#         total=0
#         for i in range(n):
#             if tag[i]=='V':
#                 total=total+5
#             if tag[i]=='L':
#                 total=total+50
#             if tag[i]=='D':
#                 total=total+500
#             if tag[i]=='M':
#                 total=total+1000
#             if i==0:
#                 if tag[i]=='I':
#                     total=total+1
#                 if tag[i]=='X':
#                     total=total+10
#                 if tag[i]=='C':
#                     total=total+100
#             else:
#                 if tag[i]=='I':
#                     if tag[i-1]=='V' or tag[i-1]=='X':
#                         total=total-1
#                     else:
#                         total=total+1
#                 if tag[i]=='X':
#                     if tag[i-1]=='L' or tag[i-1]=='C':
#                         total=total-10
#                     else:
#                         total=total+10
#                 if tag[i]=='C':
#                     if tag[i-1]=='D' or tag[i-1]=='M':
#                         total=total-100
#                     else:
#                         total=total+100
#         return total
class Solution:
    def romanToInt(self, s:str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total=0
        prev_value=0
        for char in s:
            curr_value=roman_values[char]
            if curr_value>prev_value:
                total+=curr_value-2*prev_value
            else:
                total+=curr_value
            prev_value=curr_value
        return total
sol1=Solution()
s="MCMXCIV"
print(sol1.romanToInt(s))