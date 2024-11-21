# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         strs_size=len(strs)
#         result=""
#         if strs_size==1:
#             return strs[0]
#         for i in range(1,strs_size):
#             if len(strs[i])==0:
#                 return ""
#             if i==1:
#                 compare_size=min(len(strs[0]),len(strs[i]))
#                 if compare_size==0:
#                     return ""
#                 index=compare_size
#                 for j in range(compare_size):
#                     if strs[0][j]!=strs[i][j]:
#                         index=j
#                         break
#                 result=result+strs[i][:index]
#             else:
#                 compare_size=min(len(result),len(strs[i]))
#                 index=compare_size
#                 for j in range(compare_size):
#                     if result[j]!=strs[i][j]:
#                         index=j
#                         break
#                 result=result[:index]
#         return result
    
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs_size=len(strs)
        result=""
        if strs_size==1:
            return strs[0]
        current=strs[0]
        for i in range(1,strs_size):
            if len(strs[i])==0:
                return ""
            compare_size=min(len(current),len(strs[i]))
            if compare_size==0:
                return ""
            index=compare_size
            for j in range(compare_size):
                if current[j]!=strs[i][j]:
                    index=j
                    break
            result=strs[i][:index]
            current=result
        return result
    
Solution1=Solution()
strs=["flower","flow","flight"]
print(Solution1.longestCommonPrefix(strs))