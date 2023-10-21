"""扫雷题目解答"""
from collections import deque


class Solution:
    """aaa"""

    def updateBoard(self, board, click):
        """bbb"""
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        if board[click[0]][click[1]] == "B":
            return board

        # 只在点击到未操作的非雷格时，才进行处理~
        q = deque()
        q.append(click)
        visited = []

        while q:
            cur = q.popleft()
            visited.append(cur)

            if cur[0] < 0 or cur[0] >= len(board):
                continue
            if cur[1] < 0 or cur[1] >= len(board[0]):
                continue

            mines_num = get_mines_num(board, cur)

            if board[cur[0]][cur[1]] == "E":
                if mines_num:
                    board[cur[0]][cur[1]] = str(mines_num)
                else:
                    board[cur[0]][cur[1]] = "B"
                    items = [[cur[0] + i, cur[1] + j] for i in (-1, 0, 1) for j in (-1, 0, 1)]
                    for item in items:
                        if item[0] < 0 or item[0] >= len(board):
                            continue
                        if item[1] < 0 or item[1] >= len(board[0]):
                            continue
                        if item not in visited:
                            q.append(item)

        return board


def get_mines_num(board, pos):
    """获取周围地雷数量"""
    counter = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            row = pos[0] + i
            col = pos[1] + j
            if row < 0 or row >= len(board):
                continue
            if col < 0 or col >= len(board[0]):
                continue

            if board[row][col] == "M":
                counter += 1
    return counter


b = [["E", "M", "M", "E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E", "E", "E", "E"],
     ["E", "E", "E", "E", "E", "E", "E", "E"], ["E", "M", "E", "E", "E", "E", "E", "E"],
     ["E", "E", "E", "E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E", "E", "E", "E"],
     ["E", "E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E", "E"]]
c = [5, 5]

obj = Solution()
result = obj.updateBoard(b, c)
pass
