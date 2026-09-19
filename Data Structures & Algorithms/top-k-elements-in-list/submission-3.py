class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for elem in nums:
            if elem in res:
                res[elem]+=1
            else:
                res[elem]=1
        nums_new = [0]*(len(nums)+1)
        for e,key in res.items():
            if nums_new[res[e]]:
                nums_new[res[e]].append(e)
            else:
                nums_new[res[e]] = [e]
        k_counter = 0
        final_result = []
        for i in range(len(nums_new)-1,0,-1):
            if nums_new[i] != 0:
                for e in nums_new[i]:
                    if k_counter == k:
                        break
                    final_result.append(e)
                    k_counter+=1

        return final_result