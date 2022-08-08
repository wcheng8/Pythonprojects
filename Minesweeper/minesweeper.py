import random

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0,self.dim_size**2 - 1)
            row = loc//self.dim_size
            col = loc%self.dim_size

            if board[row][col] == '*':
                continue
            board[row][col] = '*'
            bombs_planted +=1

        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)

    def get_num_neighboring_bombs(self,row,col):
        num_neighboring_bombs = 0
        for r in range(max(0,row-1),min(self.dim_size-1,(row+1)+1)):
            for c in range(max(0,col-1),max(self.dim_size-1,col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs +=1
        return num_neighboring_bombs
def play(dim_size=10, num_bombs=10):

    # Step1: create a board and plant the bombs
    board = Board(dim_size,num_bombs)
    # Step2: show the user the board and ask for where they want to dig
    # Step3a: if location is a bomb, show game over message
    # Step3b: if location is not a bomb, dig recusively until each square is at least nest to a bomb
    # Step4: Repeat steps 2 and 3ab until no more places to dig


    pass
