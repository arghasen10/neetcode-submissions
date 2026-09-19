class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = {}
        for ele in nums:
            hashset[ele] = 1
        starts=[]
        longest_length = 0
        for ele in nums:
            length = 0
            if ele-1 not in hashset:
                while ele+length in hashset:
                    length+=1
            longest_length = max(length,longest_length)
        return longest_length

