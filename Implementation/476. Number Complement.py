class Solution:
    def findComplement(self, num: int) -> int:
        len_bin_num = len(bin(num)[2:])
        temp = int("1" * len_bin_num, 2)
        return num ^ temp