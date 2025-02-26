from clear import *
import random
import os
import platform



BOARD = [['7','8','9'], ['4','5','6'],['1','2','3']]
starter =""
SAVE_FILE = "saved_game.txt"


def display_board():
    os.system('clear')
    print('Board\n-----')
    for row in BOARD:
        for cell in row:
            print(f'{cell}', end='|')
        print('\b \n')



def update_board(user_number,my_number,user_sign,my_sign):
        global BOARD
        for i in range(3):
            for j in range(3):
                if BOARD[i][j] == user_number:
                    BOARD[i][j] = user_sign
                if BOARD[i][j] == str(my_number):
                    BOARD[i][j] = my_sign

        display_board()
def check_winner():
    for row in BOARD:
        if row[0] == row[1] == row[2] and row[0] in ['x', 'o']:
            return row[0]

    for col in range(3):
        if BOARD[0][col] == BOARD[1][col] == BOARD[2][col] and BOARD[0][col] in ['x', 'o']:
            return BOARD[0][col]


    if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] and BOARD[0][0] in ['x', 'o']:
        return BOARD[0][0]

    if BOARD[0][2] == BOARD[1][1] == BOARD[2][0] and BOARD[0][2] in ['x', 'o']:
        return BOARD[0][2]

    return None #

def board_is_full():
    for i in range(3):
        for j in range(3):
            if BOARD[i][j] in ['1','2','3','4','5','6','7','8','9']:
                return False
    return True
def manage_turns(current_turn,user_sign1,user_sign2):

    if current_turn == user_sign1:
        return user_sign2
    else:
        return user_sign1

def easy():

        return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])


def medium(user_sign1, user_sign2):
    for i in range(3):
        for j in range(3):
            if BOARD[i][j] not in ['x', 'o']:
                temp = BOARD[i][j]
                BOARD[i][j] = user_sign2
                if check_winner():
                    BOARD[i][j] = temp
                    return temp
                BOARD[i][j] = temp

    for i in range(3):
        for j in range(3):
            if BOARD[i][j] not in ['x', 'o']:
                temp = BOARD[i][j]
                BOARD[i][j] = user_sign1
                if check_winner():
                    BOARD[i][j] = temp
                    return temp
                BOARD[i][j] = temp

    for i in range(3):
        for j in range(3):
            if BOARD[i][j] not in ['x', 'o']:
                return BOARD[i][j]
    return None

def hard(user_sign1, user_sign2):
    for i in range(3):
        for j in range(3):
            if BOARD[i][j] not in ['x', 'o']:
                temp = BOARD[i][j]
                BOARD[i][j] = user_sign2
                if check_winner():
                    BOARD[i][j] = temp
                    return temp
                BOARD[i][j] = temp

    for i in range(3):
        for j in range(3):
            if BOARD[i][j] not in ['x', 'o']:
                temp = BOARD[i][j]
                BOARD[i][j] = user_sign1
                if check_winner():
                    BOARD[i][j] = temp
                    return temp
                BOARD[i][j] = temp


    if BOARD[1][1] not in ['x', 'o']:
        return '5'

    for move in ['7', '9', '1', '3']:
        for i in range(3):
            for j in range(3):
                if BOARD[i][j] == move:
                    return move

            for move in ['8', '4', '6', '2']:
                for i in range(3):
                    for j in range(3):
                        if BOARD[i][j] == move:
                            return move

            return None

def set_sign_starter(user_sign1, user_sign2):
    global starter
    if user_sign1 == 'x':
        user_sign2= 'o'
    else:
        user_sign2='x'
    signs = [user_sign1, user_sign2]

    starter =  random.choice(signs)
    print("The player who starts is {}".format(starter))

    return starter

def save_game(turn, user_sign1, user_sign2,difficulty_level):
    with open(SAVE_FILE, "w") as f:
        f.write(f"{turn}\n")
        f.write(f"{user_sign1} {user_sign2}\n")
        f.write(f"{difficulty_level}\n")
        f.write(str(BOARD))
    print("Game saved successfully!")


def load_game():
    global BOARD

    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            lines = f.readlines()

        if len(lines) < 4:
            print("Save file is corrupted or outdated.")
            return None

        turn = lines[0].strip()
        user_sign1, user_sign2 = lines[1].strip().split()
        difficulty_level = lines[2].strip()
        BOARD = eval(lines[3].strip())

        print(f"Game loaded successfully! Turn: {turn}, Difficulty: {difficulty_level}")
        return turn, user_sign1, user_sign2, difficulty_level
    return None
