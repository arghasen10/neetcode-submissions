class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        final_list = []
        for ele in strs:
            key = sorted(ele)
            hashmap[tuple(key)].append(ele)
        return list(hashmap.values())
