class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        start_idx = 0
        end_idx = len(s) - 1

        def back_trace(start, end, temp_str):
            counter = 0
            if start >= end:
                return counter

            if temp_str[start] != "(":
                back_trace(start + 1, end, temp_str)
            if temp_str[end] != ")":
                back_trace(start, end + 1, temp_str)

            return end - start


obj = Solution()
test_str = "(())"
result = obj.longestValidParentheses(test_str)

assert result == 4

pass
