class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start_idx, current_partition):
            if start_idx == len(s):
                res.append(current_partition.copy())
                return

            for end_idx in range(start_idx, len(s)): 
                substring = s[start_idx : end_idx + 1]

                if substring == substring[::-1]:
                    current_partition.append(substring)
                    backtrack(end_idx + 1, current_partition)
                    current_partition.pop()

        backtrack(0, [])
        return res