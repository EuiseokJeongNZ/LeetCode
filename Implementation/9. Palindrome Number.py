# First Answer with Slicing
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = str(x)[::-1]
        if str(x) == x1:
            return True
        return False

# Second Answer not Using String Method
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # Nagative number is always Flase
            return False

        reversedNum = 0 # Number to be compared
        temp = x
        while temp != 0: # Execute when temp variable is not 0
            reversedNum = temp % 10 + reversedNum * 10 # reversing
            temp //= 10 # // Variable temp assigned quotient as much as divided by 10
        return reversedNum == x























#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reserved_num = 0
        temp = x
        while temp != 0:
            digit = temp % 10  # digit is the remainder divided by 10
            reserved_num = reserved_num * 10 + digit  # It serves to add a new digit to the number that has been flipped to date
            temp //= 10
        return reserved_num == x  # Return the boolean value whether it is Ture or Flase