class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = []
        for single_str in strs:
            final_string.append(single_str+"_;")
        result = "".join(final_string)
        return result 

    def decode(self, s: str) -> List[str]:
        strs = s.split("_;")
        return strs[:-1]
       