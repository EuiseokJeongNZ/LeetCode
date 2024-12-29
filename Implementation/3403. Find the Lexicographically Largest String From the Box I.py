class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        ans = ''
        curr = 'a'
        curr_idx_lst = []

        for i, w in enumerate(word):
            if w >= curr:
                curr = w
                curr_idx_lst.append(i)
                continue

        for i in curr_idx_lst:
            end_idx = i + len(word) - numFriends + 1
            ans = max(ans, word[i:end_idx])

        return ans

        # def generate_splits(start, word, split_num):
        #     if split_num == 1:
        #         return [[word[start:]]]

        #     splits = []

        #     for i in range(start + 1, len(word) - split_num + 2):
        #         first_word = word[start:i]
        #         rest_word = generate_splits(i, word, split_num - 1)

        #         for rest in rest_word:
        #             splits.append([first_word] + rest)

        #     return splits

        # max_string = ""
        # all_splits = generate_splits(0, word, numFriends)

        # for split in all_splits:
        #     for s in split:
        #         max_string = max(max_string, s)

        # return max_string
