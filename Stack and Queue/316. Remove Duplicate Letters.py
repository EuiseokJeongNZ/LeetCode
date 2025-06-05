class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {char: i for i, char in enumerate(s)}
        stack = []
        visited = set()
        ans = ''

        for i, char in enumerate(s):
            if char in visited:
                continue

            while stack and stack[-1][1] > char and last_index[stack[-1][1]] > i:
                stack_i, stack_char = stack.pop()
                visited.remove(stack_char)

            stack.append((i, char))
            visited.add(char)

        for i, char in stack:
            ans += char

        return ans