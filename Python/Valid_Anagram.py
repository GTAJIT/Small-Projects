class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
a = "abc"
b = "bca"
f = Solution()
f.isAnagram(a, b)