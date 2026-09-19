class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        for i in range(len(s2)):
            e = s2[i]
            if e in s1:
                sub_s = s2[i:i+len(s1)]
                if sorted(sub_s) == sorted(s1):
                    return True
        return False

        