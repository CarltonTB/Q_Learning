# Compute the Q-values for each action in each square and optimal policy given a grid-world input
# Author: Carlton Brady

from enum import Enum
from q_learning_agent import *

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
        self.reward = reward


def generate_problem_from_input(input):
    """return a 4x4 list that represents the board as well as a list that represents the requested
     output type, for example:
     ['q','11'] = output q-values for each direction at square 11
     ['p'] = output optimal policy for every square"""
    input_array = input.split(',')
    if len(input_array) < 5:
        print("INVALID INPUT: input was too short")
        return None

    goal1_location = int(input_array[0])
    goal2_location = int(input_array[1])
    forbidden_location = int(input_array[2])
    wall_location = int(input_array[3])
    output_type = [input_array[4]]
    if output_type[0] == 'q' and len(input_array) == 6:
        output_type.append(input_array[5])

    board = []
    for i in range(1, 5):
        row = []
        for j in range(1, 5):
            row.append(Square(compute_location_from_board_indices(i, j), SquareType.EMPTY))
        board.append(row)

    goal1_indices = compute_board_indices_from_location(goal1_location)
    goal2_indices = compute_board_indices_from_location(goal2_location)
    forbidden_indices = compute_board_indices_from_location(forbidden_location)
    wall_location = compute_board_indices_from_location(wall_location)

    # Add the start square in the same place every time
    board[3][1].type = SquareType.START
    # Add goal squares
    board[goal1_indices[0]][goal1_indices[1]].type = SquareType.GOAL
    board[goal1_indices[0]][goal1_indices[1]].reward = 100
    board[goal2_indices[0]][goal2_indices[1]].type = SquareType.GOAL
    board[goal2_indices[0]][goal2_indices[1]].reward = 100
    # Add forbidden square
    board[forbidden_indices[0]][forbidden_indices[1]].type = SquareType.FORBIDDEN
    board[forbidden_indices[0]][forbidden_indices[1]].reward = -100
    # Add wall square
    board[wall_location[0]][wall_location[1]].type = SquareType.WALL
    return board, output_type


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


def learn_q_values(board):
    agent = QLearningAgent(0.1, 0.1, 0.2, -0.1)
    # Start at the starting square
    agent.current_square = board[3][1]
    # take an action
    # action = agent.get_next_action()
    # reward =
    # receive a sample transition
    # update Q(s,a) for that action
    # repeat until convergence or 10,000 iterations

# problem = generate_problem_from_input("12,15,8,6,p")
# print(convert_board_to_string(problem[0]))
#
# problem2 = generate_problem_from_input("13,4,5,3,q,11")
# print(convert_board_to_string(problem2[0]))
