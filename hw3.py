# Runs Q-learning for the grid world that is passed on the command line
# Author: Carlton Brady

from q_learning import *


def main():
    input_array = []
    for i in range(1, len(sys.argv)):
        input_array.append(sys.argv[i])
    problem = generate_problem_from_input(input_array)
    if problem is not None:
        board = problem[0]
        output_type = problem[1]
        learn_q_values(board)
        if len(output_type) == 1 and output_type[0] == "p":
            print_optimal_policy_on_board(board)
            print_optimal_policy_for_all_squares(board)
        elif len(output_type) == 2 and output_type[0] == "q":
            location = int(output_type[1])
            (i, j) = compute_board_indices_from_location(location)
            print(convert_q_values_for_square_to_string(board[i][j]))
        else:
            print("Invalid output type was specified. The last 2 args should be q and the number of a square,"
                  " or the last arg should be p")


if __name__ == "__main__":
    main()