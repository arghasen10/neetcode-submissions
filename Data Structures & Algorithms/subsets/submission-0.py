class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        combination = []
        def backtrack(index):
            print(combination)
            results.append(combination.copy())
            for i in range(index, len(nums)):
                combination.append(nums[i])
                backtrack(i+1)
                combination.pop()
        backtrack(0)
        return results