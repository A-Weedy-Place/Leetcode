class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        x = count = one = two = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    one = i
                    two = j
        x = one + 1
        while x < 8:
            if board[x][two] == ".":
                 x += 1
                 continue
            if board[x][two] == "B":
                break
            if board[x][two] == "p":
                count += 1
                break
        
        x = one - 1
        while x > -1:
            if board[x][two] == ".":
                 x -= 1
                 continue
            if board[x][two] == "B":
                break
            if board[x][two] == "p":
                count += 1
                break
        
        x = two + 1
        while x < 8:
            if board[one][x] == ".":
                 x += 1
                 continue
            if board[one][x] == "B":
                break
            if board[one][x] == "p":
                count += 1
                break
        
        x = two - 1
        while x > -1:
            if board[one][x] == ".":
                 x -= 1
                 continue
            if board[one][x] == "B":
                break
            if board[one][x] == "p":
                count += 1
                break
        
        return count