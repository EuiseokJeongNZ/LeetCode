class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)

        for i in range(n - k + 1):
            temp = nums[i:k + i]
            temp.sort()
            dic = {t: temp.count(t) for t in temp}
            freq_val = [(freq, val) for val, freq in dic.items()]
            freq_val.sort(reverse=True)

            flag = x
            remaining = []

            for freq, val in freq_val:
                if freq >= x and flag > 0:
                    ans[i] += freq * val
                    flag -= 1
                else:
                    remaining.append((freq, val))

            remaining.sort(reverse=True)

            if flag != 0:
                for freq, val in remaining:
                    if flag == 0:
                        break
                    else:
                        ans[i] += freq * val
                        flag -= 1

        return ans