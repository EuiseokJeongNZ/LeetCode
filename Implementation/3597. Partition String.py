class Solution:
    def partitionString(self, s: str) -> List[str]:
        segment = set()
        ans = list()
        curr = ''

        for ch in s:
            curr += ch
            if not curr in segment:
                segment.add(curr)
                ans.append(curr)
                curr = ''

        if curr and not curr in segment:
            ans.append(curr)
        return ans