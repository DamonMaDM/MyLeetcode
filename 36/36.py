
"""
简单hashset应用
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal = [set() for x in range(9)]
        vertical = [set() for x in range(9)]
        box = [set() for x in range(9)]
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                print(value)
                b = (i//3)*3 + j//3
                if value in horizontal[i] or value in vertical[j] or value in box[b]:
                    return False
                horizontal[i].add(value)
                vertical[j].add(value)
                box[b].add(value)
        return True
