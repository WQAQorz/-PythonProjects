from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        for i in range(len(s)):
            q.append([i, i])

        while (q):
            cur = q.popleft()
            if cur[0] != 0 and s[cur[0] - 1] not in cur:
                q.append([cur[0] - 1, cur[1]])

            for _ in range(len(s)):
                pass


obj = Solution()
obj.lengthOfLongestSubstring("abcddd")

pass
