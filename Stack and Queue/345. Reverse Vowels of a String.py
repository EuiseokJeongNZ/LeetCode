class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']

        charactersStack = [i for i in s if i in vowels]
        answer = []

        for i in s:
            if i in vowels:
                answer.append(charactersStack.pop())
                continue
            answer.append(i)

        return ''.join(answer)