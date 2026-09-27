class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []
        def backtrack(start):
            result.append(subset.copy())
            for index in range(start, len(nums)):
                if index > start and nums[index] == nums[index - 1]:
                    continue
                subset.append(nums[index])
                backtrack(index+1)
                subset.pop()
        backtrack(0)
        return result