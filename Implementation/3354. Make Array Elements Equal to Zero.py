class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def check(curr, direction):
            temp = nums[:]
            move = direction
            while 0 <= curr < n:
                if move == 'left':
                    curr -= 1
                    if 0 <= curr and temp[curr] != 0:
                        temp[curr] -= 1
                        move = 'right'
                elif move == 'right':
                    curr += 1
                    if curr < len(temp) and temp[curr] != 0:
                        temp[curr] -= 1
                        move = 'left'
            return temp

        n = len(nums)
        cnt = 0

        for i in range(n):
            if nums[i] == 0:
                l = check(i, 'left')
                r = check(i, 'right')
                if l.count(0) == n:
                    cnt += 1
                if r.count(0) == n:
                    cnt += 1

        return cnt
