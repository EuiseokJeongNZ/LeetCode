class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic = {}
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.",
                 "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-",
                 ".--", "-..-", "-.--", "--.."]

        for i in range(26):
            dic[chr(ord('a') + i)] = morse[i]

        lst = []
        for w in words:
            temp = ''
            for c in w:
                temp += dic[c]

            if temp not in lst:
                lst.append(temp)

        return len(lst)