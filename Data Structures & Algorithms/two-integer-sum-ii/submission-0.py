class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}
        for i, e in enumerate(numbers):
            diff = target-e
            if diff in res:
                return [res[diff], i+1]
            res[e]=i+1
