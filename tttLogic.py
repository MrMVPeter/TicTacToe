"""
This script creates the logic for TicTacToe
"""


class Game:

    def __init__(self):
        self.state = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.turn = 'X'
        self.score = {'X':0,'O':0}

    def change_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def reset_board(self,last_move):
        self.state = [' ']*9
        self.score[last_move] += 1
        self.turn = 'X'


    def check_board(self,list):
        # Check for winner (Parent Algorithm)
        if list[0] == list[1] == list[2] and list[0] != " ":
            self.reset_board(list[0])
        elif list[3] == list[4] == list[5] and list[3] != " ":
            self.reset_board(list[3])
        elif list[6] == list[7] == list[8] and list[6] != " ":
            self.reset_board(list[6])
        elif list[0] == list[3] == list[6] and list[0] != " ":
            self.reset_board(list[0])
        elif list[1] == list[4] == list[7] and list[1] != " ":
            self.reset_board(list[1])
        elif list[2] == list[5] == list[8] and list[2] != " ":
            self.reset_board(list[2])
        elif list[0] == list[4] == list[8] and list[0] != " ":
            self.reset_board(list[0])
        elif list[6] == list[4] == list[2] and list[6] != " ":
            self.reset_board(list[6])

    def player_move(self, move):
        if self.state[move] == ' ':
            self.state[move] = self.turn
            return True
        else:
            return False
