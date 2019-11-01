# Q-Learning
Python version: 3.6  

An implementation of Q-learning for grid worlds.  
The world is a 4x4 grid with 5 special squares:  

- 2 goal squares, represented by G, which give positive reward
- 1 forbidden square, represented by F, which gives negative reward
- 1 wall square, represented by W, which the agent cannot pass through
- 1 starting square, represented by S, where the agent starts each episode (square #2)

Periods represent normal, empty squares.  
Example grid world configuration:  
.  .  G  .  
.  .  .  G  
.  W  .  F  
.  S  .  .  

The squares have a number representing their location defined as follows:  
13--14--15--16  
9---10--11--12  
5----6---7---8  
1----2---3---4  

# Running It
The program can be run by running hw3.py and passing input in the form:  
G G F W q {square number}  
or  
G G F W p  
where the first 2 args are the square locations of the goals, the third
arg is the location of the forbidden square, the 4th arg is the location of the
wall square, and the 5th/6th args are the desire output type.  

Example 1:  
python3 hw3.py 12 15 8 6 p  
Creates a grid world with goals at squares 12 and 15, forbidden square at
8, wall at 6, the output type p prints the optimal policy for all squares like so:  
Optimal policy: (grid view)  
→  →  G  ←  
→  →  →  G  
↑  W  ↑  F  
→  →  ↑  ←  

Optimal policy:  
1 →  
2 →  
3 ↑  
4 ←  
5 ←  
6 None (WALL)  
7 ↑  
8 EXIT (FORBIDDEN)  
9 →  
10 →  
11 →  
12 EXIT (GOAL)  
13 →  
14 →  
15 EXIT (GOAL)  
16 ↑  

Example 2:  
python3 hw3.py 12 15 8 6 q 11  
Creates a grid world with goals at squares 12 and 15, forbidden square at
8, wall at 6, the output type q 11 prints the q values for square 11 like so:  
location: 11  
Q-values:  
↑ 19.571323608004402  
↓ 0.6561497231644189  
→ 19.899999999999974  
← 0.57451473379369  

# Tests
The tests can be run like so:  
python3 q_learning_tests.py