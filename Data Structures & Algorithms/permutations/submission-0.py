class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        permutation = []
        used = [False] * len(nums)

        def backtrack():
            if len(permutation) == len(nums):
                results.append(permutation.copy())
                return
            for i, v in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                permutation.append(v)
                backtrack()
                permutation.pop()
                used[i] = False
        backtrack()
        return results