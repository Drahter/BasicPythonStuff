import random
import math


class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomCompPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square.')
        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, situation, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if situation.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (situation.num_empty_squares() + 1) if other_player ==  max_player \
                        else -1*(situation.num_empty_squares() + 1)
                    }

        elif not situation.empty_squares():
            return{'position': None, 'score':0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in situation.available_moves():
            #1 - сделать шаг
            situation.make_move(possible_move, player)
            #2 - просимулировать дальнейший ход игры
            sim_score = self.minimax(situation, other_player)

            #3 - отменить ход
            situation.board[possible_move] = ' '
            situation.current_winner = None
            sim_score['position'] = possible_move
            #4 - обновть переменные
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
                else:
                    if sim_score['score'] < best['score']:
                        best = sim_score

        return best

