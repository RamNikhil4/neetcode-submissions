class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for i in range(9):
            for j in range (9):
                num=board[i][j]
                if (num=='.'):
                    continue
                if num in seen:
                    return False
                seen.add(num)
            seen.clear()
        for i in range(9):
            for j in range(9):
                num= board[j][i]
                if num==".":
                    continue
                if num in seen:
                    return False
                seen.add(num)

            seen.clear()
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        num=board[i][j]
                        if(num=="."):
                            continue
                        if num in seen:
                            return False
                        seen.add(num)
                seen.clear()
        return True  