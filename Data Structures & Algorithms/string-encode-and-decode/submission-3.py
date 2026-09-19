class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for elem in strs:
            final_str += str(len(elem))+"_"+elem
        return final_str

    def decode(self, s: str) -> List[str]:
        output=[]
        i=0
        while i < len(s):
            j=i
            counter = 0
            while s[j]!= "_":
                j+=1
                counter = int(s[i:j])
                
            output.append(s[j+1:j+counter+1])
            i= j+counter+1
        return output
