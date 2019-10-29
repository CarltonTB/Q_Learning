
from enum import Enum

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
    if square.type.name == SquareType.GOAL.name or square.type.name == SquareType.GOAL.name:
        q_value_string += "EXIT "
        q_value_string += str(square.exit_q_value)
    else:
        for key in square.q_values.keys():
            q_value_string += CONST_DIRECTIONAL_CHARACTERS[key]
            q_value_string += " "
            q_value_string += str(square.q_values.get(key))
            q_value_string += "\n"

    return q_value_string

