# assignment: programming assignment 5
# author: Yazmyn Sims
# date: 12/3/2022
# file: chess.py is a program that asks a user for a chess piece and it's position and will tell you all the places that piece can move on the board.
# input: user will select a chess piece and a position on the board.
# output: the program will output x's on all the spots where the piece can move.


class Board:
    def __init__(self):
        self.board = {}
        self.empty()
    def empty(self):
        for col in 'abcdefgh':
            for row in '12345678':
                self.board[col+row] = ' '
    def set(self, pos, label):
        self.board[pos] = label
    def draw(self):
        print("\n")
        print('   a   b   c   d   e   f   g   h')
        print(' +---+---+---+---+---+---+---+---+')
        print('8| {} | {} | {} | {} | {} | {} | {} | {} |8'.format(self.board['a8'], self.board['b8'], self.board['c8'], self.board['d8'], self.board['e8'], self.board['f8'], self.board['g8'], self.board['h8'],))
        print(' +---+---+---+---+---+---+---+---+')
        print('7| {} | {} | {} | {} | {} | {} | {} | {} |7'.format(self.board['a7'], self.board['b7'], self.board['c7'], self.board['d7'], self.board['e7'], self.board['f7'], self.board['g7'], self.board['h7'],))
        print(' +---+---+---+---+---+---+---+---+')
        print('6| {} | {} | {} | {} | {} | {} | {} | {} |6'.format(self.board['a6'], self.board['b6'], self.board['c6'], self.board['d6'], self.board['e6'], self.board['f6'], self.board['g6'], self.board['h6'],))
        print(' +---+---+---+---+---+---+---+---+')
        print('5| {} | {} | {} | {} | {} | {} | {} | {} |5'.format(self.board['a5'], self.board['b5'], self.board['c5'], self.board['d5'], self.board['e5'], self.board['f5'], self.board['g5'], self.board['h5'],))
        print(' +---+---+---+---+---+---+---+---+')
        print('4| {} | {} | {} | {} | {} | {} | {} | {} |4'.format(self.board['a4'], self.board['b4'], self.board['c4'], self.board['d4'], self.board['e4'], self.board['f4'], self.board['g4'], self.board['h4'],))
        print(' +---+---+---+---+---+---+---+---+')
        print('3| {} | {} | {} | {} | {} | {} | {} | {} |3'.format(self.board['a3'], self.board['b3'], self.board['c3'], self.board['d3'], self.board['e3'], self.board['f3'], self.board['g3'], self.board['h3'],))
        print(' +---+---+---+---+---+---+---+---+')
        print('2| {} | {} | {} | {} | {} | {} | {} | {} |2'.format(self.board['a2'], self.board['b2'], self.board['c2'], self.board['d2'], self.board['e2'], self.board['f2'], self.board['g2'], self.board['h2'],))
        print(' +---+---+---+---+---+---+---+---+')
        print('1| {} | {} | {} | {} | {} | {} | {} | {} |1'.format(self.board['a1'], self.board['b1'], self.board['c1'], self.board['d1'], self.board['e1'], self.board['f1'], self.board['g1'], self.board['h1'],))
        print(' +---+---+---+---+---+---+---+---+')
        print('   a   b   c   d   e   f   g   h')
    def get_keys(self):
        return self.board.keys()

class Chess_Piece:
    def __init__(self, board, pos, color='white'):
        self.position = self.get_index(pos)
        self.color = color
        board.set(pos, self.get_name())
    def get_index(self, pos):
        return ('abcdefgh'.index(pos[0]), '12345678'.index(pos[1]))
        
    def get_name(self):
        pass
    def moves(self, board):
        pass

class King(Chess_Piece):
    def get_name(self):
        return 'K'
        pass
    def moves(self, board):
        for key in board.get_keys():
            key_index = self.get_index(key)
            if key_index == self.position:
                continue
            elif key_index[0] == self.position[0] + 1 and key_index[1] == self.position[1] + 1:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] - 1 and key_index[1] == self.position[1] - 1:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] - 1 and key_index[1] == self.position[1] + 1:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] + 1 and key_index[1] == self.position[1] - 1:
                board.set(key, 'x')

            elif key_index[0]  == self.position[0] - 1 and key_index[1] == self.position[1]:
                board.set(key, 'x')
            elif key_index[0]  == self.position[0] + 1 and key_index[1] == self.position[1]:
                board.set(key, 'x')
            elif key_index[1]  == self.position[1] - 1 and key_index[0] == self.position[0]:
                board.set(key, 'x')
            elif key_index[1]  == self.position[1] + 1 and key_index[0] == self.position[0]:
                board.set(key, 'x')
            pass

class Queen(Chess_Piece):
    def get_name(self):
        return 'Q'
        pass
    def moves(self, board):
        key_position = (self.position)
        for key in board.get_keys():
            key_index = self.get_index(key)
            if key_index == self.position:
                continue
            elif key_index[0] == self.position[0]:
                board.set(key, 'x')
            elif key_index[1] == self.position[1]:
                board.set(key, 'x')
        
        for key in board.get_keys():
            key_index = self.get_index(key)
            deno = abs(key_position[1] - key_index[1])
            deno2 = abs(key_position[0] - key_index[0])
            if deno2 == 0:
                continue
            elif (deno/deno2 == 1):
                board.set(key, 'x')
            pass
        
class Rook(Chess_Piece):
    def get_name(self):
        return 'R'
        pass
    def moves(self, board):
        for key in board.get_keys():
            key_index = self.get_index(key)
            if key_index == self.position:
                continue
            elif key_index[0] == self.position[0]:
                board.set(key, 'x')
            elif key_index[1] == self.position[1]:
                board.set(key, 'x')
            pass
        
class Bishop(Chess_Piece):
    def get_name(self):
        return 'B'
        pass
    def moves(self, board):
        key_position = (self.position)
                 
        for key in board.get_keys():
            key_index = self.get_index(key)
            deno = abs(key_position[1] - key_index[1])
            deno2 = abs(key_position[0] - key_index[0])
    
            if deno2 == 0:
                continue
            elif (deno/deno2 == 1):
                board.set(key, 'x')

class Knight(Chess_Piece):
    def get_name(self):
        return 'N'
        pass
    def moves(self, board):
        for key in board.get_keys():
            key_index = self.get_index(key)

            if key_index == self.position:
                continue
            elif key_index[0] == self.position[0] - 1 and key_index[1] == self.position[1]+ 2:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] + 1 and key_index[1] == self.position[1] + 2:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] -1 and key_index[1] == self.position[1] - 2:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] + 1 and key_index[1] == self.position[1] - 2:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] - 2 and key_index[1] == self.position[1] + 1:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] + 2 and key_index[1] == self.position[1] + 1:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] - 2 and key_index[1] == self.position[1] - 1:
                board.set(key, 'x')
            elif key_index[0] == self.position[0] + 2 and key_index[1] == self.position[1] - 1:
                board.set(key, 'x')
            pass
            
#main program
if __name__ == '__main__':

#Title
    print("Welcome to the Chess Game!")

#Create Board
    board = Board()
    board.draw()

while True:
        #Get Input
        choice = input("Enter a chess piece and its position or type X to exit:\n").lower()

        if choice != 'x' and len(choice)!= 3:
            continue
        if choice != 'x' and (choice[1] not in 'abcdefg' or choice[2] not in '12345678'):
            continue
        
        #End Program
        if choice[0] == 'r': # what goes in the indexes
            rook = Rook(board, choice[1::])
            rook.moves(board)
            board.draw()

        #bishop
        elif choice[0] == 'b':
            bishop = Bishop(board, choice[1::])
            bishop.moves(board)
            board.draw()

        #knight
        elif choice[0] == 'n':
            knight = Knight(board, choice[1::])
            knight.moves(board)
            board.draw()

        #queen
        elif choice[0] == 'q':
            queen = Queen(board, choice[1::])
            queen.moves(board)
            board.draw()

        #king
        elif choice[0] == 'k':
            king = King(board, choice[1::])
            king.moves(board)
            board.draw()
        elif choice == 'x':
            print("Goodbye!\n")
            break
        #clear board afterwards
        board.empty()
