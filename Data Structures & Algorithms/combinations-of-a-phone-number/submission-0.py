class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7":"pqrs","8": "tuv", "9": "wxyz"
        }
        
        result = []
        path = []

        def backtrack(start):
            if start == len(digits):
                result.append("".join(path))
                return
            for letter in letters[digits[start]]:
                path.append(letter)
                backtrack(start+1)
                path.pop()
        backtrack(0)
        return result