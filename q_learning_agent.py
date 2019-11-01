# Agent that takes actions in the grid world to learn q-values
# Author: Carlton Brady

import random
from q_learning_utils import *


class QLearningAgent:

    def __init__(self, learning_rate, epsilon, discount_rate, living_reward):
        self.last_square = None
        self.current_square = None
        self.next_square = None
        self.trajectory = []
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.discount_rate = discount_rate
        self.living_reward = living_reward
        self.possible_actions = ["NORTH", "SOUTH", "EAST", "WEST"]
        self.episodes = 0

    def get_next_action(self):
        """Get the next action that the agent should take based on the
        q-values of the current square and random action probability epsilon"""
        rand = random.random()
        if rand <= self.epsilon:
            return self.random_action()
        else:
            max_action, max_q = get_max_q_and_action(self.current_square)
            return max_action

    def random_action(self):
        """return a random action:
        NORTH, SOUTH, EAST, or WEST with equal probability"""
        rand_action = random.randint(0, 3)
        return self.possible_actions[rand_action]

    def take_action(self, action, board):
        """Move the agent to the appropriate next square based on the action
        it takes"""
        current_indices = compute_board_indices_from_location(self.current_square.location)
        new_i = current_indices[0]
        new_j = current_indices[1]
        moved = False
        reward = 0

        if action == "NORTH" and current_indices[0] > 0 and board[new_i - 1][new_j].type.name != SquareType.WALL.name:
            new_i -= 1
            moved = True
        elif action == "SOUTH" and current_indices[0] < 3 and board[new_i + 1][new_j].type.name != SquareType.WALL.name:
            new_i += 1
            moved = True
        elif action == "EAST" and current_indices[1] < 3 and board[new_i][new_j + 1].type.name != SquareType.WALL.name:
            new_j += 1
            moved = True
        elif action == "WEST" and current_indices[1] > 0 and board[new_i][new_j - 1].type.name != SquareType.WALL.name:
            new_j -= 1
            moved = True
        elif action == "EXIT":
            # print("Agent exited on square of type: " + self.current_square.type.value)
            reward += self.current_square.reward
            self.episodes += 1
            # Move the agent back to the starting square
            self.last_square = self.current_square
            self.current_square = board[3][1]

        else:
            # print("Action is invalid or the agent is unable to move in direction: " + action)
            reward += self.living_reward
            self.last_square = self.current_square

        if moved:
            reward += self.living_reward
            self.last_square = self.current_square
            self.current_square = board[new_i][new_j]

        self.trajectory.append(action)
        return reward

    def do_q_update(self, action, reward):
        """Based on the action the agent took to get to it's current square
        and the reward it received from that, update the q-value of the last_square.
        Return True if the Q values have converged, which we will define as the Q value
         not changing up to 2 decimal places"""
        if self.last_square is not None:
            if action == "EXIT":
                # update the exit action q value
                # since there is no next state after exiting,
                # no need to add the q value of the max q action in the next state,
                # since the next state is the starting state because the episode has ended
                self.last_square.exit_q_value = (1 - self.learning_rate) * self.last_square.exit_q_value + self.learning_rate * reward

            else:
                max_q_and_action = get_max_q_and_action(self.current_square)
                max_q = max_q_and_action[1]
                # check to see if exiting is the max action
                if self.current_square.exit_q_value > max_q:
                    max_q = self.current_square.exit_q_value

                self.last_square.q_values[action] = (1 - self.learning_rate) * self.last_square.q_values[action] + \
                        self.learning_rate * (reward + self.discount_rate * max_q)