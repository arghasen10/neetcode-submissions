class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices = {}
        for i, e in enumerate(numbers):
            indices[e] = i
        for i, e in enumerate(numbers):
            diff = target-e
            if diff in indices and indices[diff]!=i:
                return [i+1, indices[diff]+1]
                print(i,indices[diff])