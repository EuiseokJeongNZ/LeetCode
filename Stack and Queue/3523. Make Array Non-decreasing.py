from collections import deque

class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        max_lst = deque()
        cnt, curr_cnt = 0, 0

        while nums:
            last_num = nums.pop()
            if not max_lst:
                max_lst.append(last_num)
                curr_cnt += 1
            elif max_lst and last_num <= max_lst[0]:
                max_lst.appendleft(last_num)
                curr_cnt += 1
            elif max_lst and last_num > max_lst[0]:
                cnt = max(cnt, curr_cnt)
                while max_lst and last_num > max_lst[0]:
                    max_lst.popleft()
                max_lst.appendleft(last_num)
                cnt = len(max_lst)

        cnt = len(max_lst)

        return cnt