
from enum import Enum
import sys
import random

# Unicode for the arrow characters
CONST_DIRECTIONAL_CHARACTERS = {
    "NORTH": u'\u2191',
    "SOUTH": u'\u2193',
    "EAST": u'\u2192',
    "WEST": u'\u2190'
}


class SquareType(Enum):
    GOAL = "GOAL"
    WALL = "WALL"
    START = "START"
    FORBIDDEN = "FORBIDDEN"
    EMPTY = "."


class Square:

    def __init__(self, location, type, reward=0):
        self.type = type
        self.location = location
        self.q_values = {
            "NORTH": 0,
            "SOUTH": 0,
            "EAST": 0,
            "WEST": 0
        }
        self.exit_q_value = 0
        self.reward = reward


def compute_board_indices_from_location(location):
    if location % 4 == 0:
        i = 4 - (location // 4)
    else:
        i = 3 - (location // 4)
    j = (location % 4)-1
    return i, j


def compute_location_from_board_indices(i, j):
    return ((4-i)*4) + j


def get_max_q_and_action(square):
    max_q = -sys.maxsize-1
    max_action = None
    for key in square.q_values.keys():
        if square.q_values.get(key) > max_q:
            max_q = square.q_values.get(key)
            max_action = key
    # If there are multiple max actions of the same Q-value, return a random action between all of them
    max_actions = [max_action]
    for key in square.q_values.keys():
        if square.q_values.get(key) == max_q:
            max_actions.append(key)
    if len(max_actions) > 1:
        rand_max_action_index = random.randint(0, len(max_actions)-1)
        max_action = max_actions[rand_max_action_index]
    return max_action, max_q


def convert_board_to_string(board):
    board_string = ""
    for row in board:
        for column in row:
            board_string += column.type.value[0]
            board_string += "  "
        board_string += "\n"
    return board_string


def convert_q_values_for_square_to_string(square):
    """given a square, print the Q-values for each
    action possible from that square"""
    q_value_string = ""
    q_value_string += "location: " + str(square.location) + "\n"
    q_value_string += "Q-values:\n"
    if square.type.name == SquareType.GOAL.name or square.type.name == SquareType.FORBIDDEN.name:
        q_value_string += "EXIT "
        q_value_string += str(square.exit_q_value) + "\n"
    elif square.type.name == SquareType.WALL.name:
        q_value_string += "WALL (No Q-values)" + "\n"
    else:
        for key in square.q_values.keys():
            q_value_string += CONST_DIRECTIONAL_CHARACTERS[key]
            q_value_string += " "
            q_value_string += str(square.q_values.get(key)) + "\n"

    return q_value_string


def print_all_q_values_for_board(board):
    for row in board:
        for square in row:
            print(convert_q_values_for_square_to_string(square))


def print_optimal_policy_for_all_squares(board):
    print("Pi Star:")
    for i in range(3, -1, -1):
        for j in range(0, 4):
            max_action, max_q = get_max_q_and_action(board[i][j])
            if board[i][j].type.name == SquareType.GOAL.name or board[i][j].type.name == SquareType.FORBIDDEN.name:
                print(str(board[i][j].location) + " " + "EXIT" + " (" + board[i][j].type.name + ")")
            elif board[i][j].type.name == SquareType.WALL.name:
                print(str(board[i][j].location) + " " + "None" + " (" + board[i][j].type.name + ")")
            else:
                print(str(board[i][j].location) + " " + str(CONST_DIRECTIONAL_CHARACTERS.get(max_action)))
