class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        binary = ('0' * (32 - len(binary))) + binary
        reverse_binary = binary[::-1]
        sqr = 0
        res = 0

        for i in range(-1, -(len(reverse_binary) + 1), -1):
            res += (2 ** sqr) * int(reverse_binary[i])
            sqr += 1
        return res

        # Another Solution
        # res = 0
        # for _ in range(32):
        #     res = res << 1       # Step 1: Left-shift all bits in res by 1 position.
        #     rightBit = n & 1     # Step 2. Get right-most bit of N.
        #     n = n >> 1           # Step 3. Drop right-most bit we just extracted
        #     res = res | rightBit # Step 4. Append bit we extracted to end of res.        
        # return res
