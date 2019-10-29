import unittest
from q_learning import *
from q_learning_agent import *
from q_learning_utils import *


class QLearningTests(unittest.TestCase):

    def test_problem_generation(self):
        test_problem = generate_problem_from_input("12,15,8,6,p")
        board_string = convert_board_to_string(test_problem[0])
        board_list = board_string.split("  ")
        self.assertEqual("G", board_list[2])
        self.assertEqual("G", board_list[7])
        self.assertEqual("F", board_list[11])
        self.assertEqual("W", board_list[9])
        self.assertEqual("S", board_list[13])
        self.assertEqual('p', test_problem[1][0])

        test_problem2 = generate_problem_from_input("13,4,5,3,q,11")
        board_string2 = convert_board_to_string(test_problem2[0])
        board_list2 = board_string2.split("  ")
        self.assertEqual("G", board_list2[0])
        self.assertEqual("G", board_list2[15])
        self.assertEqual("\nF", board_list2[8])
        self.assertEqual("W", board_list2[14])
        self.assertEqual("S", board_list2[13])
        self.assertEqual('q', test_problem2[1][0])
        self.assertEqual('11', test_problem2[1][1])

        # problem = generate_problem_from_input("12,15,8,6,p")
        # print(convert_board_to_string(problem[0]))
        #
        # problem2 = generate_problem_from_input("13,4,5,3,q,11")
        # print(convert_board_to_string(problem2[0]))

    def test_get_next_action(self):
        agent = QLearningAgent(0.1, 0, 0.2, -0.1)
        test_problem = generate_problem_from_input("12,15,8,6,p")
        board = test_problem[0]
        agent.current_square = board[3][1]
        agent.current_square.q_values["WEST"] = 1.0
        action = agent.get_next_action()
        self.assertEqual(action, "WEST")
        agent.current_square.q_values["EAST"] = 1.01
        action = agent.get_next_action()
        self.assertEqual(action, "EAST")

    def test_q_update(self):
        agent = QLearningAgent(0.1, 0.1, 0.2, -0.1)
        test_problem = generate_problem_from_input("12,15,8,6,p")
        board = test_problem[0]
        agent.current_square = board[3][1]

        action = "EAST"
        reward = agent.take_action(action, board)
        agent.do_q_update(action, reward)
        self.assertEqual(-0.1, round(reward, 1))

        action = "NORTH"
        reward = agent.take_action(action, board)
        agent.do_q_update(action, reward)
        self.assertEqual(-0.1, round(reward, 1))

        reward = agent.take_action(action, board)
        agent.do_q_update(action, reward)
        self.assertEqual(-0.1, round(reward, 1))

        reward = agent.take_action(action, board)
        agent.do_q_update(action, reward)
        self.assertEqual(-0.1, round(reward, 1))

        action = "EXIT"
        reward = agent.take_action(action, board)
        agent.do_q_update(action, reward)
        self.assertEqual(100, round(reward, 1))
        self.assertEqual(agent.current_square.location, 2)

        # exit_q_string = convert_q_values_for_square_to_string(agent.last_square)
        # print(exit_q_string)
        # exit_q_string2 = convert_q_values_for_square_to_string(board[3][1])
        # print(exit_q_string2)


if __name__ == '__main__':
    unittest.main()
