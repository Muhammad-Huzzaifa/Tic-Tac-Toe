from typing import List

class TicTacToe:
    ''' A Tic-Tac-Toe game implementation with AI using the Minimax algorithm and Alpha-Beta pruning.
    '''


    def __init__(self) -> None:
        ''' Initializes the Tic-Tac-Toe board as a 3x3 grid filled with spaces.
        '''

        self.board = [[' ' for _ in range(3)] for _ in range(3)]


    def XPlayerWinCheck(self) -> bool:
        ''' Check if the X player has won the game.

        Returns:
            bool: True if the X player has won the game, False otherwise.
        '''

        for i in range(3):
            if all(self.board[i][j] == 'X' for j in range(3)) or all(self.board[j][i] == 'X' for j in range(3)):
                return True
        
        if all(self.board[i][i] == 'X' for i in range(3)) or all(self.board[i][2-i] == 'X' for i in range(3)):
            return True
        
        return False


    def OPlayerWinCheck(self) -> bool:
        ''' Check if the O player has won the game.
        
        Returns:
            bool: True if the O player has won the game, False otherwise.
        '''

        for i in range(3):
            if all(self.board[i][j] == 'O' for j in range(3)) or all(self.board[j][i] == 'O' for j in range(3)):
                return True
        
        if all(self.board[i][i] == 'O' for i in range(3)) or all(self.board[i][2-i] == 'O' for i in range(3)):
            return True
        
        return False


    def DrawCheck(self) -> bool:
        '''Check if the game is a draw.

        Returns:
            bool: True if the game is a draw, False otherwise.
        '''

        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))


    def XPlayerMove(self, x : int, y : int) -> bool:
        ''' Make a move for the X player.

        Args:
            x (int): The x-coordinate of the move.
            y (int): The y-coordinate of the move.
        
        Returns:
            bool: True if the move was successful, False otherwise
        '''

        if self.board[x][y] == ' ':
            self.board[x][y] = 'X'
            return True
        
        return False


    def OPlayerMove(self, x : int, y : int) -> bool:
        ''' Make a move for the O player.

        Args:
            x (int): The x-coordinate of the move.
            y (int): The y-coordinate of the move.

        Returns:
            bool: True if the move was successful, False otherwise
        '''

        if self.board[x][y] == ' ':
            self.board[x][y] = 'O'
            return True
        
        return False


    def getBoard(self) -> List[List[str]]:
        ''' Get the current state of the board.
        '''

        return self.board
    

    def minimax(self, isMaximizing : bool, alpha : int, beta : int) -> int:
        ''' The Minimax algorithm with Alpha-Beta pruning to determine the best move for the AI player.

        Args:
            isMaximizing (bool): Whether the current player is maximizing (True) or minimizing (False).
            alpha (int): The alpha value for the Alpha-Beta pruning.
            beta (int): The beta value for the Alpha-Beta pruning.

        Returns:
            int: The best score for the current player.
        '''

        if self.XPlayerWinCheck():
            return 1
        if self.OPlayerWinCheck():
            return -1
        if self.DrawCheck():
            return 0
        
        if isMaximizing:
            maxValue = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        value = self.minimax(False, alpha, beta)
                        self.board[i][j] = ' '
                        maxValue = max(maxValue, value)
                        alpha = max(alpha, value)
                        if alpha >= beta:
                            break
            return maxValue

        else:
            minValue = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'O'
                        value = self.minimax(True, alpha, beta)
                        self.board[i][j] = ' '
                        minValue = min(minValue, value)
                        beta = min(beta, value)
                        if alpha >= beta:
                            break
            return minValue
        
    
    def bestMove(self, isMaximizing : bool) -> tuple:
        ''' Get the best move for the AI player.

        Args:
            isMaximizing (bool): Whether the AI player is maximizing (True) or minimizing (False).

        Returns:
            tuple: The best move for the AI player.
        '''

        bestScore = float('-inf') if isMaximizing else float('inf')
        bestMove = (-1, -1)

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'X' if isMaximizing else 'O'
                    score = self.minimax(not isMaximizing, float('-inf'), float('inf'))
                    self.board[i][j] = ' '
                    if isMaximizing:
                        if score > bestScore:
                            bestScore = score
                            bestMove = (i, j)
                    else:
                        if score < bestScore:
                            bestScore = score
                            bestMove = (i, j)
        
        return bestMove