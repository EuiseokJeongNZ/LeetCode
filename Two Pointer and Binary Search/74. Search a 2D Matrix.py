class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            lt = 0
            rt = len(i) - 1
            while lt <= rt:
                mid = (lt + rt) // 2
                if i[mid] < target:
                    lt = mid + 1
                elif i[mid] > target:
                    rt = mid - 1
                else:
                    return True
        return False
