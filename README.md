AI Programming Assignment
Name: Aryan C
Roll Number: SE24UCSE033
Course: Artificial Intelligence
Overview
This repository contains implementations of:
Turing Test Design
CAPTCHA System Design
Water Jug Problem using BFS and DFS
All programs are implemented in Python 3 without external libraries.
1️⃣ Assignment 1: Turing Test Design (turing_test.md)
This module explains the architecture and working of the Turing Test.
Objective
To demonstrate how a machine attempts to imitate human conversation and how a judge evaluates responses to determine whether the entity is human or artificial.
Components
Human – Gives natural, emotional, and contextual responses.
Machine – Generates programmed or rule-based responses.
Judge – Evaluates responses and decides whether they are human or machine.
Working Principle
Human / Machine → Judge → Decision
The judge interacts without knowing which is human or machine.
If the judge cannot reliably distinguish them, the machine is said to pass the Turing Test.
How to View
Open:
Turing_Captcha/turing_test.md
2️⃣ Assignment 2: CAPTCHA System (captcha.md, captcha_demo.py)
Implements a simple CAPTCHA mechanism to distinguish humans from bots.
Objective
To design a security mechanism that allows human users to pass while blocking automated programs.
CAPTCHA Types Implemented
Type	Example	Purpose
Math	What is 15 + 9?	Arithmetic reasoning
Logic	What comes after Monday?	Common knowledge
Text	Enter code: ABX9P	Character recognition
Architecture
User → Challenge Generated → User Response → Verification → Access Granted / Blocked
How to Run
cd Turing_Captcha
python3 captcha_demo.py
Sample Output
Session ID : 3F82AB91CD
Challenge  : What is 15 + 9?
Response   : 24
Result     : Access Granted.
3️⃣ Assignment 3: Water Jug Problem (water_jug.py)
Solve the classic Water Jug Problem using uninformed search strategies.
Problem Description
We are given two jugs:
Jug1 capacity = 4 litres
Jug2 capacity = 3 litres
Goal: Measure exactly 2 litres.
Initial State: (0, 0)
Goal Condition: Either jug contains 2 litres.
State Representation
State is represented as:
(x, y)
Where:
x = water in Jug1
y = water in Jug2
Example:
(4, 2)
Actions
Fill Jug1
Fill Jug2
Empty Jug1
Empty Jug2
Pour Jug1 → Jug2
Pour Jug2 → Jug1
Algorithms Implemented
1️⃣ Breadth-First Search (BFS)
Uses a Queue (FIFO)
Explores level by level
Complete
Guarantees shortest path (optimal solution)
Higher memory usage
2️⃣ Depth-First Search (DFS)
Uses a Stack (LIFO)
Explores deep first
Lower memory usage
Not guaranteed optimal
How to Run
cd Search
python3 water_jug.py
Sample Output
---- BFS ----
(0, 0)
(0, 3)
(3, 0)
(3, 3)
(4, 2)

---- DFS ----
(0, 0)
(0, 3)
(3, 0)
(3, 3)
(4, 2)
Performance Comparison
Algorithm	Time Complexity	Space Complexity
BFS	O(b^d)	O(b^d)
DFS	O(b^d)	O(d)
Where:
b = branching factor
d = depth of solution
Observations
BFS guarantees optimal solution.
DFS may find solution faster depending on order.
BFS uses more memory than DFS.
Requirements
Python 3
No external libraries required
Conclusion
This assignment demonstrates:
Human vs machine differentiation (Turing Test)
Security validation using CAPTCHA
Problem solving using uninformed search algorithms
All implementations follow modular design and standard AI search principles.
