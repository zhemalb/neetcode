from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in range(len(nums)):
            n = len(a)
            a.add(nums[i])
            if len(a) == n:
                return True

        return False
