class Solution:
    def bitwiseComplement(self, n: int) -> int:
        len_bin_num = len(bin(n)[2:])
        temp = int("1" * len_bin_num, 2)
        return n ^ temp
