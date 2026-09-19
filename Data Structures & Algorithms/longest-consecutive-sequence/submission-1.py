class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_sorted = sorted(nums)
        lowest = nums[0]
        result = 1
        old_result=1
        for e in range(1,len(nums_sorted)):
            if nums_sorted[e] == nums_sorted[e-1]+1:
                result+=1
            elif nums_sorted[e] == nums_sorted[e-1]:
                continue
            else:
                if old_result<result:
                    old_result=result
                result=1
        return max(old_result,result)

