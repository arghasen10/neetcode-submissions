class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        combination = []

        def backtrack(start, remaining):
            if remaining == 0:
                results.append(combination.copy())
                return
            for index in range(start, len(candidates)):
                value = candidates[index]
                if index > start and value == candidates[index-1]:
                    continue
                if value > remaining:
                    break
                combination.append(value)
                backtrack(index+1, remaining- value)
                combination.pop()
        backtrack(0, target)
        return results