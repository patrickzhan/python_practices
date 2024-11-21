# class Solution:
#     def isValid(self, s: str) -> bool:
#         parentheses_list=[]
#         if s:
#             for char in list(s):
#                 if char=='(' or char=='[' or char=='{':
#                     parentheses_list.append(char)
#                 if char==')':
#                     if len(parentheses_list)==0:
#                         return False
#                     if parentheses_list[-1]=='(':
#                         parentheses_list.pop(-1)
#                     else:
#                         return False
#                 if char==']':
#                     if len(parentheses_list)==0:
#                         return False
#                     if parentheses_list[-1]=='[':
#                         parentheses_list.pop(-1)
#                     else:
#                         return False
#                 if char=='}':
#                     if len(parentheses_list)==0:
#                         return False
#                     if parentheses_list[-1]=='{':
#                         parentheses_list.pop(-1)
#                     else:
#                         return False
#             return not parentheses_list
#         else:
#             return True


class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_list=[]
        parentheses_dict={')':'(',']':'[','}':'{'}
        if s:
            for char in list(s):
                if char=='(' or char=='[' or char=='{':
                    parentheses_list.append(char)
                if char==')' or char==']' or char=='}':
                    if len(parentheses_list)==0:
                        return False
                    
                    if parentheses_list[-1]==parentheses_dict[char]:
                        parentheses_list.pop(-1)
                    else:
                        return False
            return not parentheses_list
        else:
            return True

Solution1=Solution()
example="()[]{}"
result=Solution1.isValid(example)
print(result)