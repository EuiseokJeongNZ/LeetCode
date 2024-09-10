class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        dic = {i: ord(i) for i in sorted(set(letters))}

        for i, j in dic.items():
            if j <= ord(target):
                continue
            return i

        return letters[0]
