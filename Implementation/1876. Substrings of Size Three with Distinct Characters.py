class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt = 0

        for i in range(3, len(s) + 1):
            window = s[i - 3: i]
            flag = False
            for w in window:
                if window.count(w) >= 2:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                cnt += 1

        return cnt