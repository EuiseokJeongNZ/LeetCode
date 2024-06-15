class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []

        for word in words:
            lower = word.lower()
            frst = False
            scnd = False
            thrd = False

            for l in lower:
                if l in 'qwertyuiop':
                    frst = True
                    continue
                if l in 'asdfghjkl':
                    scnd = True
                    continue
                if l in 'zxcvbnm':
                    thrd = True

            if (frst and not scnd and not thrd) or (not frst and scnd and not thrd) or (not frst and not scnd and thrd):
                ans.append(word)

        return ans