class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


isAnagram = Solution()

print(isAnagram.isAnagram("racecar", "carrace"))
