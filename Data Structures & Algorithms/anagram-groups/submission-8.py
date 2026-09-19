class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict()

        for e in strs:
            if tuple(sorted(e)) in hashmap:
                hashmap[tuple(sorted(e))].append(e)
            else:
                hashmap[tuple(sorted(e))] = [e]
        arr = []
        for k, v in hashmap.items():
            arr.append(v)
        return arr

