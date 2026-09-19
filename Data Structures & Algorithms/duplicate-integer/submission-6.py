class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for e in nums:
            if e in hashmap:
                return True
            hashmap[e] = 1
        return False