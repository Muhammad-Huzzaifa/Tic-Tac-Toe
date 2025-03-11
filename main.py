import pygame
import sys
import random
from TicTacToe import TicTacToe

class TicTacToeGame:
    ''' A Tic-Tac-Toe game implementation using Pygame.
    '''


    def __init__(self) -> None:
        ''' Initialize the game window and variables.
        '''

        pygame.init()
        self.width, self.height = 420, 490
        self.screen = pygame.display.set_mode( (self.width, self.height) )
        pygame.display.set_caption('Tic Tac Toe')
        
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.gray = (50, 50, 50)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)

        self.backColor = (20, 20, 20)
        self.textColor = self.white
        
        self.largeFont = pygame.font.SysFont('Comic Sans MS', 28)
        self.smallFont = pygame.font.SysFont('Comic Sans MS', 21)
        
        self.boxSize = 140
        self.gameLogic = TicTacToe()
        self.running = True
        self.over = False
        self.isX = True
        self.playerTurn = True
        self.vsComputer = True
        self.currPlayer = 'X'
        self.statusText = ''
        self.statusColor = self.white
        

    def draw_board(self) -> None:
        ''' Draw the Tic-Tac-Toe board.
        '''

        self.screen.fill(self.backColor)
    
        statusSurface = self.largeFont.render(self.statusText, True, self.statusColor)
        statusRect = statusSurface.get_rect(center=(self.width // 2, 35))
        self.screen.blit(statusSurface, statusRect)
        
        pygame.draw.line(self.screen, self.white, (self.boxSize, 70), (self.boxSize, self.height), 2)
        pygame.draw.line(self.screen, self.white, (self.boxSize * 2, 70), (self.boxSize * 2, self.height), 2)
        pygame.draw.line(self.screen, self.white, (0, 70 + self.boxSize), (self.width, 70 + self.boxSize), 2)
        pygame.draw.line(self.screen, self.white, (0, 70 + self.boxSize * 2), (self.width, 70 + self.boxSize * 2), 2)
        
        board = self.gameLogic.getBoard()
        for i in range(3):
            for j in range(3):
                x = j * self.boxSize + self.boxSize // 2
                y = i * self.boxSize + 70 + self.boxSize // 2
                
                if board[i][j] == 'X':
                    pygame.draw.line(self.screen, self.white, (x - 42, y - 42), (x + 42, y + 42), 3)
                    pygame.draw.line(self.screen, self.white, (x + 42, y - 42), (x - 42, y + 42), 3)
                elif board[i][j] == 'O':
                    pygame.draw.circle(self.screen, self.white, (x, y), 42, 3)
    

    def draw_game_options(self) -> None:
        ''' Draw the game options screen.
        '''

        self.screen.fill(self.backColor)
        
        title = self.largeFont.render('Tic Tac Toe', True, self.white)
        titleRect = title.get_rect(center=(self.width // 2, 75))
        self.screen.blit(title, titleRect)
        
        vsHumanBtn = pygame.Rect(105, 200, 210, 56)
        vsAIBtn = pygame.Rect(105, 270, 210, 56)

        pygame.draw.rect(self.screen, self.gray, vsHumanBtn)
        pygame.draw.rect(self.screen, self.gray, vsAIBtn)
        
        vsHumanText = self.smallFont.render('Player vs Player', True, self.white)
        vsAIText = self.smallFont.render('Player vs Computer', True, self.white)
        
        self.screen.blit(vsHumanText, vsHumanText.get_rect(center=vsHumanBtn.center))
        self.screen.blit(vsAIText, vsAIText.get_rect(center=vsAIBtn.center))
        
        pygame.display.flip()
        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    if vsHumanBtn.collidepoint(mouse_pos):
                        self.vsComputer = False
                        return
                    elif vsAIBtn.collidepoint(mouse_pos):
                        self.vsComputer = True
                        return
    
    
    def coin_toss(self) -> bool:
        ''' Perform a coin toss.
        '''

        self.screen.fill(self.backColor)
        
        title = self.largeFont.render('Coin Toss', True, self.white)
        title_rect = title.get_rect(center=(self.width // 2, 75))
        self.screen.blit(title, title_rect)
        
        Head = pygame.Rect(105, 200, 210, 56)
        Tail = pygame.Rect(105, 270, 210, 56)
        
        pygame.draw.rect(self.screen, self.gray, Head)
        pygame.draw.rect(self.screen, self.gray, Tail)
        
        HeadText = self.smallFont.render('Heads', True, self.white)
        TailText = self.smallFont.render('Tails', True, self.white)
        
        self.screen.blit(HeadText, HeadText.get_rect(center=Head.center))
        self.screen.blit(TailText, TailText.get_rect(center=Tail.center))
        
        pygame.display.flip()
        
        choice = None

        while choice is None:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    mousePos = event.pos
                    if Head.collidepoint(mousePos):
                        choice = 'Heads'
                    elif Tail.collidepoint(mousePos):
                        choice = 'Tails'
        
        result = random.choice(['Heads', 'Tails'])
        
        self.screen.fill(self.backColor)
        result_text = self.largeFont.render(f'Coin shows: {result}', True, self.white)
        result_rect = result_text.get_rect(center=(self.width // 2, 200))
        self.screen.blit(result_text, result_rect)
        
        win_or_lose = 'YOU WON!' if choice == result else 'YOU LOST!'
        outcome_text = self.largeFont.render(win_or_lose, True, self.green if choice == result else self.red)
        outcome_rect = outcome_text.get_rect(center=(self.width // 2, 270))
        self.screen.blit(outcome_text, outcome_rect)
        
        pygame.display.flip()
        pygame.time.delay(1500)
        
        return choice == result
    

    def choose_symbol(self) -> bool:
        ''' Let the player choose their symbol.
        '''

        self.screen.fill(self.backColor)
        
        title = self.largeFont.render('Choose your symbol', True, self.white)
        titleRect = title.get_rect(center=(self.width // 2, 70))
        self.screen.blit(title, titleRect)
        
        XBtn = pygame.Rect(105, 200, 210, 56)
        OBtn = pygame.Rect(105, 270, 210, 56)
        
        pygame.draw.rect(self.screen, self.gray, XBtn)
        pygame.draw.rect(self.screen, self.gray, OBtn)
        
        XText = self.largeFont.render('X', True, self.white)
        OText = self.largeFont.render('O', True, self.white)
        
        self.screen.blit(XText, XText.get_rect(center=XBtn.center))
        self.screen.blit(OText, OText.get_rect(center=OBtn.center))
        
        pygame.display.flip()
        
        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    mouse_pos = event.pos
                    if XBtn.collidepoint(mouse_pos):
                        return True
                    elif OBtn.collidepoint(mouse_pos):
                        return False
    

    def ai_choose_symbol(self) -> bool:
        ''' Let the AI choose its symbol.
        '''

        return random.choice([True, False])
    

    def get_mouse_cell(self, pos : tuple) -> tuple:
        x, y = pos
        if y < 70:
            return None
        
        row = (y - 70) // self.boxSize
        col = x // self.boxSize
        
        if 0 <= row < 3 and 0 <= col < 3:
            return (int(row), int(col))
        return None
    

    def make_ai_move(self) -> None:
        ''' Make a move for the AI.
        '''

        self.statusText = 'AI THINKING...'
        self.draw_board()
        pygame.display.flip()
        
        pygame.time.delay(random.randint(800, 1600))
        
        isMaximizing = self.currPlayer == 'X'
        move = self.gameLogic.bestMove(isMaximizing)
        
        if self.currPlayer == 'X':
            self.gameLogic.XPlayerMove(move[0], move[1])
        else:
            self.gameLogic.OPlayerMove(move[0], move[1])
            
        self.currPlayer = 'O' if self.currPlayer == 'X' else 'X'
        self.playerTurn = True
    

    def check_game_state(self) -> None:
        ''' Check the game state and update the status text.
        '''

        if self.gameLogic.XPlayerWinCheck():
            winner = 'PLAYER 1' if not self.vsComputer else ('YOU' if self.isX else 'AI')
            self.statusText = f'{winner} WINS!'
            self.statusColor = self.green if (self.isX and self.vsComputer) or not self.vsComputer else self.red
            self.over = True

        elif self.gameLogic.OPlayerWinCheck():
            winner = 'PLAYER 2' if not self.vsComputer else ('YOU' if not self.isX else 'AI')
            self.statusText = f'{winner} WINS!'
            self.statusColor = self.green if (not self.isX and self.vsComputer) or not self.vsComputer else self.red
            self.over = True

        elif self.gameLogic.DrawCheck():
            self.statusText = 'GAME IS DRAW!'
            self.statusColor = self.blue
            self.over = True

        else:
            if self.vsComputer:
                self.statusText = 'YOUR TURN...' if self.playerTurn else 'AI THINKING...'
            else:
                playerNum = '1' if self.currPlayer == 'X' else '2'
                self.statusText = f'PLAYER {playerNum}\'S TURN'
            self.statusColor = self.white
    

    def show_replay_options(self):
        ''' Show the replay options.
        '''
        
        replayBtn = pygame.Rect(105, 200, 210, 56)
        quit_btn = pygame.Rect(105, 270, 210, 56)
        
        pygame.draw.rect(self.screen, self.gray, replayBtn)
        pygame.draw.rect(self.screen, self.gray, quit_btn)
        
        replay_text = self.smallFont.render('Replay', True, self.white)
        quit_text = self.smallFont.render('Quit', True, self.white)
        
        self.screen.blit(replay_text, replay_text.get_rect(center=replayBtn.center))
        self.screen.blit(quit_text, quit_text.get_rect(center=quit_btn.center))
        
        pygame.display.flip()
        
        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if replayBtn.collidepoint(mouse_pos):
                        return True
                    elif quit_btn.collidepoint(mouse_pos):
                        return False
    

    def reset_game(self) -> None:
        ''' Reset the game state.
        '''

        self.gameLogic = TicTacToe()
        self.over = False
        self.currPlayer = 'X'
        self.statusText = ''
        self.statusColor = self.white
    

    def run(self) -> None:
        ''' Run the game loop.
        '''

        while self.running:

            self.draw_game_options()
            self.reset_game()
            
            if self.vsComputer:

                playerWonToss = self.coin_toss()
                
                if playerWonToss:
                    self.isX = self.choose_symbol()
                else:
                    self.isX = self.ai_choose_symbol()
                    symbolText = 'X' if self.isX else 'O'
                    
                    self.screen.fill(self.backColor)
                    
                    choiceText = self.largeFont.render(f'AI chose: {symbolText}', True, self.white)
                    choiceRect = choiceText.get_rect(center=(self.width // 2, 200))
                    self.screen.blit(choiceText, choiceRect)
                    
                    youText = self.largeFont.render(f'You are: {'O' if self.isX else 'X'}', True, self.white)
                    youRect = youText.get_rect(center=(self.width // 2, 270))
                    self.screen.blit(youText, youRect)
                    
                    pygame.display.flip()
                    pygame.time.delay(1500)
                
                self.playerTurn = self.isX
                
            clock = pygame.time.Clock()
            while not self.over:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN and not self.over:
                        

                        if (self.playerTurn and self.vsComputer) or (not self.vsComputer):
                            cell = self.get_mouse_cell(event.pos)
                            if cell:
                                row, col = cell
                                moveSuccess = False
                                
                                if self.currPlayer == 'X':
                                    moveSuccess = self.gameLogic.XPlayerMove(row, col)
                                else:
                                    moveSuccess = self.gameLogic.OPlayerMove(row, col)
                                
                                if moveSuccess:
                                    self.currPlayer = 'O' if self.currPlayer == 'X' else 'X'
                                    if self.vsComputer:
                                        self.playerTurn = False
                
                self.check_game_state()
                
                if self.vsComputer and not self.playerTurn and not self.over:
                    self.make_ai_move()
                    self.check_game_state()
                
                self.draw_board()
                
                if self.over:
                    pygame.time.delay(1000)
                    if not self.show_replay_options():
                        self.running = False
                        break
                    else:
                        break
                
                pygame.display.flip()
                clock.tick(60)
        
        pygame.quit()


if __name__ == '__main__':
    game = TicTacToeGame()
    game.run()