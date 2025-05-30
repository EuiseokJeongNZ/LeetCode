from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter_p = Counter(p)
        counter_s = Counter()
        p_sum = sum(list(counter_p.values()))
        s_sum = 0
        ans_lst = list()
        n, left, right = len(s), 0, 0

        while right < n:
            temp = s[right]
            if temp in p:
                counter_s[temp] = counter_s.get(temp, 0) + 1
                s_sum += 1
                if p_sum == s_sum:
                    if counter_p == counter_s:
                        ans_lst.append(left)
                    counter_s[s[left]] -= 1
                    left += 1
                    s_sum -= 1
                right += 1
            else:
                counter_s = Counter()
                right += 1
                left = right
                s_sum = 0

        return ans_lst