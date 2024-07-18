class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = []
        for i in range(0, len(s), 2 * k):
            ans.append(s[i:i + k][::-1])
            ans.append(s[i + k:i + 2 * k])
        return ''.join(ans)
