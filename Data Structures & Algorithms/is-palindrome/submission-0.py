class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(e for e in s if e.isalnum())
        rev_s = new_s[::-1]

        if rev_s.lower() == new_s.lower():
            return True
        else:
            return False