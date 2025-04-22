class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(values)
        visited = [False] * n
        curr, score = 0, 0

        while 0 <= curr < n and not visited[curr]:
            visited[curr] = True

            if instructions[curr] == 'jump':
                curr += values[curr]
            elif instructions[curr] == 'add':
                score += values[curr]
                curr += 1

        return score