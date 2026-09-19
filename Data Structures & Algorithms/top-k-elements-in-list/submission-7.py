from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = Counter(nums).most_common(k)
        print(freq_map)
        return [x[0] for x in freq_map]
        # hashmap = {}
        # for e in nums:
        #     hashmap[e] = 1 + hashmap.get(e,0) 
        # val_to_key = {}
        # for key,val in hashmap.items():
        #     if val in val_to_key:
        #         val_to_key[val].append(key)
        #     else:
        #         val_to_key[val] = [key]
        # keys = val_to_key.keys()
        # keys_sorted = sorted(keys,reverse=True)
        # final_output = []
        # counter=0
        # for key in keys_sorted:
        #     for e in val_to_key[key]:
        #         counter+=1
        #         if counter>k:
        #             break
        #         final_output.append(e)
                
                
                
        # return final_output
        