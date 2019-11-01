# Compute the Q-values for each action in each square and optimal policy given a grid-world input
# Author: Carlton Brady

from enum import Enum
from q_learning_agent import *
from q_learning_utils import *


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


def learn_q_values(board):
    agent = QLearningAgent(0.1, 0.1, 0.2, -0.1)
    # Start at the starting square
    agent.current_square = board[3][1]
    print("Agent is learning Q-values...")
    iterations = 0
    while iterations < 10000:
        # take an action and receive reward
        action = agent.get_next_action()
        reward = agent.take_action(action, board)
        # receive a sample transition and do Q update
        agent.do_q_update(action, reward)
        iterations += 1


# test_problem = generate_problem_from_input("12,15,8,6,p")
# board = test_problem[0]
# learn_q_values(board)
# print_optimal_policy_on_board(board)
# print_optimal_policy_for_all_squares(board)
# print_all_q_values_for_board(board)
