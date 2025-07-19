class Solution:
    def isValid(self, word: str) -> bool:
        vowels = 'AEIOUaeiou'
        num = '0123456789'
        count_char = 0

        consonant = False
        vowel = False

        for w in word:
            count_char += 1
            if 65<=ord(w)<=90 or 97<=ord(w)<=122:
                if not w in vowels:
                    consonant = True
                else:
                    vowel = True
            elif not w in num:
                return False

        if count_char >= 3:
            return consonant and vowel
        return False