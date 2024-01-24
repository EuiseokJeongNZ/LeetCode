class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def combination(index, arr):
            if index == len(digits):
                res.append(''.join(list(arr)))
                return

            for i in dic[digits[index]]:
                arr.append(i)
                combination(index+1, arr)
                arr.pop()

        if len(digits) == 0:
            return []

        dic = {
            '2':"abc", '3':"def", 
            '4':"ghi", '5':"jkl", '6':"mno",
            '7':"pqrs", '8':"tuv", '9':"wxyz"
        }
        temp = ''
        for i in digits:
            temp += dic[i]
        res = []

        combination(0, [])

        return res