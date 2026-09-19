class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap=defaultdict(list)
        
        for i, elem in enumerate(strs):
            vocab = [0]*26
            for e in elem:
                vocab[ord(e)-ord('a')]+=1
            if tuple(vocab) in hashMap:
                hashMap[tuple(vocab)].append(strs[i])
            else:
                hashMap[tuple(vocab)] = [strs[i]]
        final_list = [val for k, val in hashMap.items()]
        return final_list