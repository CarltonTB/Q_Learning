import unittest
from q_learning import *


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


if __name__ == '__main__':
    unittest.main()
