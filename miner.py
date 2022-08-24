import random

class board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #создание поля
        #функция - помощник
        self.board = self.make_new_board()
        self.assign_values_to_board()

        #создание пустого множества для хранения пар координат
        #уже проверенных мест
        self.dug = set()

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in \
                 range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size # ряд определяется количеством целых делений
            col = loc % self.dim_size  # столбец остатком от деления

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        #назначение позициям на доске числовых параметров
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)


    def get_num_neighboring_bombs(self, row, col):
        pass






def play(dim_size=10, num_bombs=10):
    #1-создать поле и расставить бомбы
    #2-нарисовать поле пользователю и узнать, куда копать
    #3-если выкопана бомба, то написать СМЭРТЬ,
    #  если не бомба, то копать дальше
    #4-если копать некуда, то ПОБЕДА
    pass





