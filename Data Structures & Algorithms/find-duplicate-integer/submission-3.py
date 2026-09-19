class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_s = sorted(nums)
        for i in range(1,len(nums_s)):
            if nums_s[i-1] == nums_s[i]:
                return nums_s[i]

        