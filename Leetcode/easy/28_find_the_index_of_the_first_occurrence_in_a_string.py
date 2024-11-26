class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_size=len(needle)
        haystack_size=len(haystack)
        if needle in haystack and not needle_size==0:
            for i in range(haystack_size):
                if haystack[i]==needle[0]:
                    if haystack[i:i+needle_size]==needle:
                        return i
        else:
            return -1


Solution1=Solution()
haystack="sadbutsad"
needle="sad"
print(Solution1.strStr(haystack,needle))
