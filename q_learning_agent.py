# Agent that takes actions in the grid world to learn q-values
# Author: Carlton Brady

import random
import q_learning


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

    def get_next_action(self):
        """Get the next action that the agent should take based on the
        q-values of the current square and random action probability epsilon"""
        if self.current_square.type.name == q_learning.SquareType.GOAL or self.current_square.type.name == q_learning.SquareType.FORBIDDEN:
            return "EXIT"

        rand = random.random()
        if rand <= self.epsilon:
            return self.random_action()
        else:
            max_q = 0
            max_key = None
            for key in self.current_square.q_values.keys():
                if round(self.current_square.q_values.get(key), 2) > round(max_q, 2):
                    max_q = self.current_square.q_values.get(key)
                    max_key = key

            if max_key is None:
                return self.random_action()
            else:
                return max_key

    def random_action(self):
        """return a random action:
        NORTH, SOUTH, EAST, or WEST with equal probability"""
        rand_action = random.randint(0, 3)
        return self.possible_actions[rand_action]

    def take_action(self, action, board):
        """Move the agent to the appropriate next square based on the action
        it takes"""
        current_indices = q_learning.compute_board_indices_from_location(self.current_square.location)
        new_i = current_indices[0]
        new_j = current_indices[1]
        moved = False
        reward = self.living_reward

        if action == "NORTH" and current_indices[0] > 0 and board[new_i-1][new_j].type.name != q_learning.SquareType.WALL:
            new_i -= 1
            moved = True
        elif action == "SOUTH" and current_indices[0] < 3 and board[new_i+1][new_j].type.name != q_learning.SquareType.WALL:
            new_i += 1
            moved = True
        elif action == "EAST" and current_indices[1] < 3 and board[new_i][new_j+1].type.name != q_learning.SquareType.WALL:
            new_j += 1
            moved = True
        elif action == "WEST" and current_indices[1] > 0 and board[new_i][new_j-1].type.name != q_learning.SquareType.WALL:
            new_j -= 1
            moved = True
        elif action == "EXIT":
            print("Agent exited on square of type: " + self.current_square.type.value)
            reward += self.current_square.reward
            # Move the agent back to the starting square
            self.last_square = self.current_square
            self.current_square = board[3][1]

        else:
            print("Action is invalid or the agent is unable to move in direction: " + action)

        if moved:
            self.last_square = self.current_square
            self.current_square = board[new_i][new_j]

        self.trajectory.append(action)
        return reward

    def do_q_update(self, action, reward):
        """Based on the action the agent took to get to it's current square
        and the reward it recieved from that, update the q-value of the last_square"""
        max_q = 0
        for key in self.current_square.q_values.keys():
            if round(self.current_square.q_values.get(key), 2) > round(max_q, 2):
                max_q = self.current_square.q_values.get(key)

        self.last_square.q_values[action] = (1-self.learning_rate) * self.last_square.q_values[action] + self.learning_rate * (reward + self.discount_rate * max_q)